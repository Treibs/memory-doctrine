---
id: B4-index-store-split
type: axiom
cluster: B-retrieval
title: A sparse index pattern-completes into a rich store — never merge them
statement: >
  Retrieval requires two functionally incompatible stores: a sparse, fast-write index
  that pattern-completes from a partial cue, and a rich, distributed content store.
  Proven twice independently — hippocampal indexing theory (Teyler & DiScenna 1986)
  and catastrophic-interference / complementary-learning-systems (McClelland,
  McNaughton & O'Reilly 1995). RAG's index/document split is engineering lineage of
  the same design. KPM = index; research/ = store; retrieval = two-stage.
domain: systems-taxonomy
generativity: 5
confidence: 0.92
status: locked
relations:
  derives-from: [B1-spreading-activation, B2-cue-dependence]
  supports: [E1-layered-distillation]
  generalizes: []
  contradicts: []
  applies-to-kpm: [two-tier-architecture, index-store-separation]
evidence: [teyler-1986-hippocampal-index, mcclelland-1995-cls]
provenance: memory-research/engram-consolidation-deep
verification: {challenged: true, citations_checked: true, gate: "rt1+purge"}
---

# B4 · A sparse index pattern-completes into a rich store — never merge them

The index/store split is not an engineering convention — it is a design forced by
**functional incompatibility** at two independent levels of description.

**Level 1 — Biology.** Teyler & DiScenna (1986) established hippocampal indexing
theory: the hippocampus "does not contain the content of an experience but provides
an index that allows the content to be retrieved." During encoding, neocortical
feature areas activate a unique distributed pattern; the hippocampus stores a sparse
pointer-set to those regions. Retrieval is a two-stage pattern completion: a partial
cue hits the sparse index → the index reinstates the rich neocortical content (Goode
et al. 2020). The dentate gyrus labels only ~6% of eligible cells per context — the
index is deliberately sparse. See [[teyler-1986-hippocampal-index]].

**Level 2 — Computational learning theory.** A single store optimized for rapid,
one-shot encoding of specific patterns cannot simultaneously serve as a store for
slow, interleaved abstraction of general regularities — the stores are *functionally
incompatible*. McClelland, McNaughton & O'Reilly (1995) proved this formally:
interleaved learning in the neocortex requires many passes; the hippocampus handles
fast one-shot binding to avoid catastrophic interference in the slow store. See
[[mcclelland-1995-cls]].

The same split appears in software under different names: RAG (index → document
fetch), HippoRAG (explicitly modeled on hippocampal indexing), LSM-tree (write-ahead
log → compacted store). The convergence is lineage, not independent re-derivation —
but the biological and computational proofs are genuine.

**KPM mapping:**
| Biology | KPM |
|---|---|
| Hippocampal index (sparse) | The KPM axiom-set + curated links |
| Neocortical store (rich, distributed) | `research/` evidence files |
| Pattern completion from partial cue | Spreading activation from query cue |
| Replay (offline batch) | Consolidation cron: re-walk + promote |

This axiom is supported by [[B1-spreading-activation]] (pattern completion is
energy-descent retrieval) and [[B2-cue-dependence]] (the index must encode
anticipated retrieval cues). It in turn supports [[E1-layered-distillation]] — the
distillation pattern that keeps the index tier compact and the store tier rich.

Evidence: [[teyler-1986-hippocampal-index]], [[mcclelland-1995-cls]].
