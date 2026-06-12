"""Relate stage — typed edges between distilled axioms (doctrine E2).

The doctrine's #1 thesis is that value lives in the *connections*, not the
nodes; a package of disconnected axioms is doctrine-shaped without being
doctrine-embodying (REVIEW.md EFF-1). This stage proposes and independently
verifies typed edges between the distilled axioms, then writes them into each
``AxiomNote.relations`` in place so ``assemble`` ships a web, not a bag.

Design adapted from ``kpm_builder.relate`` (the Builder's proven Relate
machinery): propose with ONE call that sees all (id, statement) pairs, verify
each candidate edge with an independent refute-framed call that sees only the
two statements, default to dropping an edge, and isolate per-edge failures so
one blown call can't discard the verified rest.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import Dict, List

from .llm import CompleteJSON
from .llm_core import coerce_result_dict
from .split import AxiomNote

#: The four inter-axiom relation types (``applies-to-kpm`` is package-level).
RELATION_TYPES = ("supports", "derives-from", "generalizes", "contradicts")

_MEANING: Dict[str, str] = {
    "supports": "FROM gives an independent evidential or argumentative reason to believe TO.",
    "derives-from": "FROM is a consequence or specialization derivable from the more-fundamental TO.",
    "generalizes": "FROM is the broader statement and TO is a special case of FROM.",
    "contradicts": "FROM and TO cannot both be true.",
}

PROPOSE_SCHEMA: dict = {
    "type": "object",
    "properties": {
        "relations": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "from_id": {"type": "string"},
                    "to_id": {"type": "string"},
                    "type": {"type": "string", "enum": list(RELATION_TYPES)},
                    "rationale": {"type": "string"},
                },
                "required": ["from_id", "to_id", "type"],
            },
        },
    },
    "required": ["relations"],
    "additionalProperties": False,
}

VERIFY_SCHEMA: dict = {
    "type": "object",
    "properties": {
        "holds": {"type": "boolean"},
        "reason": {"type": "string"},
    },
    "required": ["holds", "reason"],
    "additionalProperties": False,
}

_PROPOSE_SYSTEM = """\
You connect ideas. Below is a list of axioms (id: statement) from one knowledge
package. Propose DIRECTED typed relations BETWEEN axioms — never an axiom to
itself. Use only these types, with these exact directional meanings:
- supports      : FROM gives an independent reason to believe TO.
- derives-from  : FROM is derivable from the more-fundamental TO.
- generalizes   : FROM is the broader statement; TO is a special case of FROM.
- contradicts   : FROM and TO cannot both be true.
Propose at most 5 edges out of any single axiom. Only propose a relation you are
confident a skeptical reviewer would confirm; an independent verifier will check
each one and drop the rest. Output JSON only."""

_VERIFY_SYSTEM = """\
You are a skeptical, independent reviewer. A relation between two ideas has been
PROPOSED. Your job is to find a concrete reason it does NOT hold in the stated
direction. Answer holds=true ONLY if, after genuinely trying, you cannot find
any such reason. Default to holds=false when uncertain, when the link is merely
topical, or when the direction is wrong. Use only the information below."""


@dataclass
class RelateStats:
    """Honest accounting for the relate pass (nothing dropped silently)."""

    proposed: int = 0   # candidate edges the proposer suggested
    verified: int = 0   # edges that survived independent verification
    capped: int = 0     # candidates dropped by the out-degree/global caps
    skipped: int = 0    # candidates skipped on per-edge verify failure


def _propose_prompt(axioms: List[AxiomNote]) -> str:
    listing = "\n".join(f"- {a.id}: {a.statement}" for a in axioms)
    return f"{_PROPOSE_SYSTEM}\n\nAXIOMS:\n{listing}\n\nRespond with JSON only."


def _verify_prompt(rtype: str, from_stmt: str, to_stmt: str) -> str:
    return (
        f"{_VERIFY_SYSTEM}\n\n"
        f"PROPOSED RELATION:  FROM  {rtype}  TO\n"
        f"MEANING: {_MEANING[rtype]}\n"
        f"FROM: {from_stmt}\n"
        f"TO: {to_stmt}\n"
        'Respond with JSON only: {"holds": <bool>, "reason": <one sentence>}.'
    )


def _enforce_f2(a: AxiomNote, b: AxiomNote) -> None:
    """Two locked axioms may not contradict (doctrine F2): an unresolved
    contradiction means neither side is settled, so the weaker-confidence side
    returns to ``provisional``. Logged — a belief demotion is never silent."""
    if a.status == "locked" and b.status == "locked":
        weaker = a if a.confidence <= b.confidence else b
        weaker.status = "provisional"
        print(
            f"warning: relate: unresolved contradiction {a.id} <-> {b.id}; "
            f"demoting weaker '{weaker.id}' to provisional (F2)",
            file=sys.stderr,
        )


def relate_axioms(
    axioms: List[AxiomNote],
    complete_json: CompleteJSON,
    *,
    max_out_degree: int = 5,
    global_cap: int = 200,
) -> RelateStats:
    """Propose, verify, and write typed inter-axiom edges in place.

    Mutates each surviving edge into ``axiom.relations[type]``. Guards drop
    self-loops, unknown ids, and duplicates; the out-degree and global caps
    bound cost. A verify call that fails is skipped (logged, counted) so one
    blown call cannot discard the rest — and an unverifiable edge is simply
    not asserted ("default false on doubt").
    """
    stats = RelateStats()
    if len(axioms) < 2:
        return stats

    by_id = {a.id: a for a in axioms}
    raw = coerce_result_dict(
        complete_json(_propose_prompt(axioms), PROPOSE_SCHEMA),
        stage="relate",
        required_key="relations",
    )
    rows = raw.get("relations") or []
    if not isinstance(rows, list):
        rows = []

    # Guards: well-formed rows, known endpoints, no self-loops, no duplicates.
    seen: set = set()
    candidates: List[tuple] = []
    for row in rows:
        if not isinstance(row, dict):
            continue
        rtype = row.get("type")
        from_id = str(row.get("from_id", ""))
        to_id = str(row.get("to_id", ""))
        if rtype not in RELATION_TYPES or from_id == to_id:
            continue
        if from_id not in by_id or to_id not in by_id:
            continue
        key = (from_id, to_id, rtype)
        if key in seen:
            continue
        seen.add(key)
        candidates.append(key)
    stats.proposed = len(candidates)

    out_degree: Dict[str, int] = {}
    kept: List[tuple] = []
    for from_id, to_id, rtype in candidates:
        if out_degree.get(from_id, 0) >= max_out_degree or len(kept) >= global_cap:
            stats.capped += 1
            continue
        out_degree[from_id] = out_degree.get(from_id, 0) + 1
        kept.append((from_id, to_id, rtype))

    for from_id, to_id, rtype in kept:
        try:
            result = coerce_result_dict(
                complete_json(
                    _verify_prompt(rtype, by_id[from_id].statement, by_id[to_id].statement),
                    VERIFY_SCHEMA,
                ),
                stage="relate",
                required_key="holds",
            )
        except Exception as exc:  # noqa: BLE001 - isolate per edge, keep the rest
            stats.skipped += 1
            print(
                f"warning: relate: verify failed for {from_id} -{rtype}-> {to_id}, "
                f"skipping edge: {exc}",
                file=sys.stderr,
            )
            continue
        if bool(result.get("holds")):
            by_id[from_id].relations.setdefault(rtype, []).append(to_id)
            stats.verified += 1
            if rtype == "contradicts":
                _enforce_f2(by_id[from_id], by_id[to_id])
    if stats.skipped:
        print(f"warning: relate: skipped {stats.skipped} edge(s) on verify failure", file=sys.stderr)
    return stats
