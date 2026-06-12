"""Cluster stage — DETERMINISTIC thematic grouping of related axioms (EFF-4).

The doctrine organizes axioms into themes; a produced package should too.
After the relate pass has established verified typed edges, the connected
components of that relation graph ARE the package's emergent themes — no LLM
call needed. Each multi-axiom component becomes a cluster note, and every
member axiom gets a ``cluster:`` pointer (the lint validates it resolves).

Axioms with no verified edges stay uncluttered (no ``cluster:`` field): a
singleton "theme" carries no navigational value, and the doctrine treats the
cluster pointer as optional.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

from .split import AxiomNote, _RELATION_KEYS, _slugify


@dataclass
class ClusterNote:
    """A thematic cluster note: id + title + the member axiom ids."""

    id: str
    title: str
    members: List[str] = field(default_factory=list)


def _components(axioms: List[AxiomNote]) -> List[List[AxiomNote]]:
    """Connected components over the (undirected) verified relation graph."""
    by_id = {a.id: a for a in axioms}
    adjacent: Dict[str, set] = {a.id: set() for a in axioms}
    for a in axioms:
        for key in _RELATION_KEYS:
            if key == "applies-to-kpm":
                continue
            for tgt in (a.relations or {}).get(key) or []:
                if tgt in by_id:
                    adjacent[a.id].add(tgt)
                    adjacent[tgt].add(a.id)

    seen: set = set()
    components: List[List[AxiomNote]] = []
    for a in axioms:  # input order keeps output deterministic
        if a.id in seen:
            continue
        stack, comp = [a.id], []
        seen.add(a.id)
        while stack:
            nid = stack.pop()
            comp.append(by_id[nid])
            for nxt in sorted(adjacent[nid]):
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        components.append(comp)
    return components


def cluster_axioms(axioms: List[AxiomNote]) -> List[ClusterNote]:
    """Group related axioms into clusters and set their ``cluster:`` pointers.

    Mutates each member axiom's ``cluster`` attribute in place and returns the
    cluster notes for ``assemble`` to write. Deterministic: identical input
    (axioms + relations) always yields identical clusters.
    """
    clusters: List[ClusterNote] = []
    taken: set = set()
    for comp in _components(axioms):
        if len(comp) < 2:
            continue
        # Title the theme after the component's most confident axiom.
        anchor = max(comp, key=lambda a: (a.confidence, a.id))
        base = f"theme-{_slugify(anchor.title, max_words=5)}"
        cid = base
        n = 1
        while cid in taken:
            n += 1
            cid = f"{base}-{n}"
        taken.add(cid)
        note = ClusterNote(id=cid, title=anchor.title, members=[a.id for a in comp])
        for a in comp:
            a.cluster = cid
        clusters.append(note)
    return clusters


def render_cluster(cluster: ClusterNote) -> str:
    """Render a cluster note: doctrine-schema frontmatter + member wikilinks."""
    fm = (
        "---\n"
        f"id: {cluster.id}\n"
        "type: cluster\n"
        f"title: \"Theme: {cluster.title}\"\n"
        "---\n"
    )
    links = "\n".join(f"- [[{m}]]" for m in cluster.members)
    body = f"\n# Theme: {cluster.title}\n\nMember axioms:\n\n{links}\n"
    return fm + body
