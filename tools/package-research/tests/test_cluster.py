"""Tests for the cluster stage (EFF-4) — deterministic, no LLM, no API key."""

from __future__ import annotations

from package_research.assemble import assemble
from package_research.cluster import ClusterNote, cluster_axioms, render_cluster
from package_research.split import AxiomNote, EvidenceNote, _empty_relations


def _axiom(aid: str, confidence: float = 0.7) -> AxiomNote:
    return AxiomNote(
        id=aid,
        type="axiom",
        title=f"Title of {aid}",
        statement=f"Statement of {aid}.",
        confidence=confidence,
        generativity=3,
        status="candidate",
        relations=_empty_relations(),
        evidence=["ev-1"],
        provenance="package-research/distilled",
    )


def test_connected_components_become_clusters():
    a, b, c, d = (_axiom(x) for x in ("a-1", "a-2", "a-3", "a-4"))
    a.relations["supports"] = ["a-2"]
    c.relations["contradicts"] = ["a-4"]
    clusters = cluster_axioms([a, b, c, d])
    assert len(clusters) == 2
    assert {tuple(sorted(cl.members)) for cl in clusters} == {("a-1", "a-2"), ("a-3", "a-4")}
    assert a.cluster == b.cluster and a.cluster is not None
    assert c.cluster == d.cluster and c.cluster != a.cluster


def test_singletons_get_no_cluster():
    a, b = _axiom("a-1"), _axiom("a-2")   # no edges at all
    assert cluster_axioms([a, b]) == []
    assert a.cluster is None and b.cluster is None


def test_cluster_titled_after_most_confident_member():
    a, b = _axiom("a-1", confidence=0.5), _axiom("a-2", confidence=0.9)
    a.relations["supports"] = ["a-2"]
    (cluster,) = cluster_axioms([a, b])
    assert "a-2" in cluster.title


def test_clustering_is_deterministic():
    def build():
        a, b, c = (_axiom(x) for x in ("a-1", "a-2", "a-3"))
        a.relations["supports"] = ["a-2"]
        b.relations["supports"] = ["a-3"]
        return [a, b, c]

    first = cluster_axioms(build())
    second = cluster_axioms(build())
    assert [(c.id, c.members) for c in first] == [(c.id, c.members) for c in second]


def test_render_cluster_links_members():
    text = render_cluster(ClusterNote(id="theme-x", title="X", members=["a-1", "a-2"]))
    assert "id: theme-x" in text and "type: cluster" in text
    assert "[[a-1]]" in text and "[[a-2]]" in text


def test_assemble_writes_clusters_and_axiom_pointers(tmp_path):
    a, b = _axiom("a-1"), _axiom("a-2")
    a.relations["supports"] = ["a-2"]
    clusters = cluster_axioms([a, b])
    ev = EvidenceNote(id="ev-1", type="evidence", ref="n.md", supports=["a-1", "a-2"], snippets=["s"])
    assemble([a, b], [ev], tmp_path, run_date="2026-06-12", clusters=clusters)
    cluster_files = list((tmp_path / "clusters").glob("*.md"))
    assert len(cluster_files) == 1
    ax_text = (tmp_path / "axioms" / "a-1.md").read_text()
    assert f"cluster: {a.cluster}" in ax_text


def test_assemble_drops_cluster_when_members_dropped(tmp_path):
    """An axiom with no resolvable evidence is dropped; its cluster must not
    ship half-empty or leave a dangling pointer (lint would reject it)."""
    a, b = _axiom("a-1"), _axiom("a-2")
    b.evidence = ["ghost-ev"]                  # b will be dropped by assemble
    a.relations["supports"] = ["a-2"]
    clusters = cluster_axioms([a, b])
    ev = EvidenceNote(id="ev-1", type="evidence", ref="n.md", supports=["a-1"], snippets=["s"])
    result = assemble([a, b], [ev], tmp_path, run_date="2026-06-12", clusters=clusters)
    assert result.clusters_written == []
    assert "cluster:" not in (tmp_path / "axioms" / "a-1.md").read_text()


def test_assemble_strips_relations_to_dropped_axioms(tmp_path):
    """A verified edge whose target axiom was dropped (no evidence) must not
    ship dangling — the lint rejects unresolvable relation targets."""
    a, b = _axiom("a-1"), _axiom("a-2")
    b.evidence = ["ghost-ev"]
    a.relations["supports"] = ["a-2"]
    ev = EvidenceNote(id="ev-1", type="evidence", ref="n.md", supports=["a-1"], snippets=["s"])
    assemble([a, b], [ev], tmp_path, run_date="2026-06-12")
    text = (tmp_path / "axioms" / "a-1.md").read_text()
    assert "supports: []" in text
    assert "[[a-2]]" not in text
