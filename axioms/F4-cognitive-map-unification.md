---
id: F4-cognitive-map-unification
type: axiom
cluster: F-meta
title: B1 and B4 are the same object — the hippocampal cognitive map
statement: >
  Embeddings-as-geometry (B1) and the sparse-index→rich-store split (B4) are
  STRUCTURALLY the same object: the hippocampal/entorhinal cognitive map, which
  simultaneously encodes a metric geometry of meaning (grid cells fire for
  abstract 2-D conceptual spaces — Constantinescu 2016) and acts as a sparse
  index that pattern-completes to stored content (O'Keefe & Nadel 1978;
  Teyler & DiScenna 1986). A KPM is structurally a factorized cognitive map —
  relational structure (generators / index) factored from content (evidence /
  store). The biology→software step is a structural correspondence, not an
  identity: whether high-dimensional discrete KG embeddings inherit grid
  structure or only a metric is unsettled.
domain: spatial-cognitive-maps
generativity: 5
confidence: 0.83
status: locked
relations:
  derives-from: [A3-foundherentist-generativity]
  supports: [B1-spreading-activation, B4-index-store-split, E1-layered-distillation]
  generalizes: [B1-spreading-activation, B4-index-store-split]
  contradicts: []
  applies-to-kpm: [index-geometry, factorization, retrieval-as-navigation]
evidence: [constantinescu-2016-grid-concepts, behrens-2018-cognitive-map, okeefe-nadel-1978-hippocampus]
provenance: memory-research/spatial-cognitive-maps-deep
verification: {challenged: true, citations_checked: true, gate: "rt1+purge"}
---

# F4 · B1 and B4 are the same object — the hippocampal cognitive map

The doctrine has two retrieval axioms that appeared complementary but separate:

- **[[B1-spreading-activation]]**: retrieval is energy-descent pattern completion;
  the continuous-Hopfield update equals transformer attention; the embedding space
  is a *geometry* where similarity = distance.
- **[[B4-index-store-split]]**: a sparse hippocampal index pattern-completes into
  a rich content store; index and store must be kept separate to avoid catastrophic
  interference (McClelland CLS 1995; Teyler & DiScenna 1986).

The spatial-cognitive-maps beat
reveals these are **structurally the same object**: the hippocampal/entorhinal cognitive
map.

**The unification, step by step:**

1. **O'Keefe & Nadel (1978)** established that the hippocampus IS a cognitive map —
   an allocentric (world-centered), metric representation of space that simultaneously
   provides episodic context. Evidence: [[okeefe-nadel-1978-hippocampus]]. The same
   structure that is the *index* (B4: pattern-completes to stored episodes) IS the
   *geometric map* (B1: positions/similarity in a coordinate space).

2. **Constantinescu, O'Reilly & Behrens (2016)** demonstrated with fMRI that humans
   navigating a 2-D *conceptual* space (morphing bird neck/leg dimensions) produce the
   hexagonal, grid-like signal — in entorhinal cortex and vmPFC — that *physical* spatial
   navigation produces. Evidence: [[constantinescu-2016-grid-concepts]]. The grid code
   is not spatially exclusive; it operates on abstract conceptual geometry. B1's
   "embeddings-as-geometry" is therefore not a borrowed analogy — it is the predicted
   substrate.

3. **Behrens et al. (2018)** defined the cognitive map as a representation of
   *relational structure* factorized from specific *content* — the factorization being
   precisely what allows structural knowledge to transfer across environments ("solutions
   to new tasks do not have to be learnt afresh"). Evidence: [[behrens-2018-cognitive-map]].
   This factorization IS the KPM architecture: generators/index (structure) in the KPM;
   elaboration/evidence (content) in `research/` (store). B4's split is the engineering
   realization of this factorization.

**A KPM is structurally a factorized cognitive map.** The portable axiom-set is the
structural map (the relational generators that transfer across domains); the evidence
store is the content layer that fills the map's locations on demand via B1-style
pattern completion. This is the deepest theoretical justification of the whole program.
The factorization explains *why* generative axioms transfer: they carry relational
structure, not content, and structure reuses.

**Guardrails:**

- The biology→software correspondence is *structural*, not *identity*. Constantinescu
  2016 shows a grid code for 2-D *continuous* concept spaces. Whether high-dimensional,
  discrete KG embeddings inherit hexagonal grid structure or only a metric property is
  unsettled (see Open Problem S2 in the spatial beat). Confidence 0.83 reflects this.
- The map specifies *where to look*, never *whether true* — [[C2-three-orderings]] and
  [[B4-index-store-split]] guardrail stands. Geometric similarity is a navigation ordering,
  orthogonal to evidential confidence.
- HippoRAG's explicit modeling on hippocampal indexing (cited in [[B4-index-store-split]])
  is a borrowed convergence with the engram literature, not an independent derivation —
  it does not add an independent F1 corroboration point.

The unification generalizes both [[B1-spreading-activation]] and [[B4-index-store-split]]:
both are instances of the cognitive map operating at different levels of description
(geometric metric / pattern-completion index). Supporting [[E1-layered-distillation]]:
the 5-layer card's structure (generator on top, evidence below) mirrors the factorized
map (structure / content split). The factorized-map picture itself derives from
[[A3-foundherentist-generativity]]'s distinction between structural generators and
evidential content.
