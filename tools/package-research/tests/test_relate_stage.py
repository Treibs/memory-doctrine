"""Tests for the package-research relate stage (EFF-1) — no API key needed."""

from __future__ import annotations

import re

import pytest

from package_research.llm_core import reset_malformed
from package_research.relate import (
    PROPOSE_SCHEMA,
    VERIFY_SCHEMA,
    RelateStats,
    relate_axioms,
)
from package_research.split import AxiomNote, _empty_relations
from package_research.assemble import render_axiom


def _axiom(aid: str, statement: str) -> AxiomNote:
    return AxiomNote(
        id=aid,
        type="axiom",
        title=aid,
        statement=statement,
        confidence=0.7,
        generativity=3,
        status="candidate",
        relations=_empty_relations(),
        evidence=["ev-1"],
        provenance="package-research/distilled",
    )


def _proposer(rows, verify=lambda prompt: {"holds": True, "reason": "ok"}):
    def fake(prompt, schema):
        if schema is PROPOSE_SCHEMA:
            return {"relations": rows}
        if schema is VERIFY_SCHEMA:
            return verify(prompt)
        raise AssertionError("unexpected schema")

    return fake


@pytest.fixture(autouse=True)
def _clean_counters():
    reset_malformed()


def test_relate_writes_verified_edges_in_place():
    a, b = _axiom("a-one", "All X are Y."), _axiom("a-two", "This X is Y.")
    rows = [{"from_id": "a-one", "to_id": "a-two", "type": "generalizes", "rationale": "r"}]
    stats = relate_axioms([a, b], _proposer(rows))
    assert a.relations["generalizes"] == ["a-two"]
    assert stats == RelateStats(proposed=1, verified=1, capped=0, skipped=0)


def test_relate_guards_drop_self_loops_unknown_ids_and_dupes():
    a, b = _axiom("a-one", "s1"), _axiom("a-two", "s2")
    rows = [
        {"from_id": "a-one", "to_id": "a-one", "type": "supports"},          # self-loop
        {"from_id": "a-one", "to_id": "ghost", "type": "supports"},          # unknown id
        {"from_id": "a-one", "to_id": "a-two", "type": "bogus-type"},        # unknown type
        {"from_id": "a-one", "to_id": "a-two", "type": "supports"},
        {"from_id": "a-one", "to_id": "a-two", "type": "supports"},          # duplicate
        "not even a dict",
    ]
    stats = relate_axioms([a, b], _proposer(rows))
    assert stats.proposed == 1
    assert a.relations["supports"] == ["a-two"]


def test_relate_refuted_edges_are_not_written():
    a, b = _axiom("a-one", "s1"), _axiom("a-two", "s2")
    rows = [{"from_id": "a-one", "to_id": "a-two", "type": "supports"}]
    stats = relate_axioms([a, b], _proposer(rows, verify=lambda p: {"holds": False, "reason": "no"}))
    assert stats.verified == 0
    assert a.relations["supports"] == []


def test_relate_isolates_per_edge_verify_failures(capsys):
    a, b, c = _axiom("a-one", "s1"), _axiom("a-two", "s2"), _axiom("a-three", "s3")
    rows = [
        {"from_id": "a-one", "to_id": "a-two", "type": "supports"},
        {"from_id": "a-two", "to_id": "a-three", "type": "supports"},
    ]
    state = {"n": 0}

    def verify(prompt):
        state["n"] += 1
        if state["n"] == 1:
            raise RuntimeError("provider blew up")
        return {"holds": True, "reason": "ok"}

    stats = relate_axioms([a, b, c], _proposer(rows, verify=verify))
    assert stats.skipped == 1
    assert stats.verified == 1                     # second edge survived
    assert b.relations["supports"] == ["a-three"]
    assert "skipping edge" in capsys.readouterr().err


def test_relate_malformed_propose_is_counted_not_fatal(capsys):
    a, b = _axiom("a-one", "s1"), _axiom("a-two", "s2")
    stats = relate_axioms([a, b], lambda p, s: "garbage")
    assert stats == RelateStats()
    assert "malformed output" in capsys.readouterr().err


def test_relate_out_degree_cap():
    axioms = [_axiom(f"a-{i}", f"s{i}") for i in range(8)]
    rows = [
        {"from_id": "a-0", "to_id": f"a-{i}", "type": "supports"} for i in range(1, 8)
    ]
    stats = relate_axioms(axioms, _proposer(rows), max_out_degree=5)
    assert stats.capped == 2
    assert len(axioms[0].relations["supports"]) == 5


def test_relate_single_axiom_is_a_noop_without_llm_call():
    def boom(prompt, schema):
        raise AssertionError("must not be called")

    assert relate_axioms([_axiom("a-one", "s")], boom) == RelateStats()


def test_render_axiom_ships_relations_and_wikilinks():
    a = _axiom("a-one", "s1")
    a.relations["supports"] = ["a-two"]
    a.relations["contradicts"] = ["a-three"]
    text = render_axiom(a, ["ev-1"])
    assert "supports: [a-two]" in text
    assert "contradicts: [a-three]" in text
    assert "[[a-two]]" in text and "[[a-three]]" in text   # lint's wikilink rule
    assert re.search(r"(?m)^status: candidate$", text)


def test_contradiction_between_locked_axioms_demotes_weaker(capsys):
    """F2: a verified contradicts edge between two locked axioms demotes the
    lower-confidence side to provisional (the contradiction is unresolved)."""
    a, b = _axiom("a-one", "X is true."), _axiom("a-two", "X is false.")
    a.status = b.status = "locked"
    a.confidence, b.confidence = 0.9, 0.75
    rows = [{"from_id": "a-one", "to_id": "a-two", "type": "contradicts"}]
    relate_axioms([a, b], _proposer(rows))
    assert a.status == "locked"
    assert b.status == "provisional"
    assert "demoting weaker" in capsys.readouterr().err
