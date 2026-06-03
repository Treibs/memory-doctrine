---
id: B2-cue-dependence
type: axiom
cluster: B-retrieval
title: Retrieval is cue-dependent — recall equals cue–trace overlap
statement: >
  A memory trace is accessible only to the degree the retrieval cue reinstates the
  specific encoding context; cue effectiveness is determined at encoding, not by the
  cue's general semantic strength (Tulving & Thomson 1973 encoding-specificity
  principle: recall = f(cue ∩ trace)).
domain: cognitive-psych
generativity: 5
confidence: 0.90
status: locked
relations:
  derives-from: [B1-spreading-activation]
  supports: [B4-index-store-split, C2-three-orderings]
  generalizes: []
  contradicts: []
  applies-to-kpm: [retrieval-indexing, query-context-match]
evidence: [tulving-1973-encoding-specificity]
provenance: memory-research/cognitive-psych
verification: {challenged: true, citations_checked: true, gate: "rt1+purge"}
---

# B2 · Retrieval is cue-dependent — recall equals cue–trace overlap

Retrieval is not a lookup against a universal key; it is a **JOIN** between the
encoding context and the retrieval context. A weak cue that reinstates the original
encoding conditions outperforms a semantically stronger cue that does not — this is
the encoding-specificity principle, demonstrated cleanly by Tulving & Thomson (1973)
and replicated as one of the most robust findings in cognitive psychology.

The result is deeply consequential for KPM design: **index for the future question,
not for the source material.** Store each axiom with the cues and query-shapes under
which it will be retrieved. An axiom encoded for one use-case (cue type) may fail for
a differently-shaped query — not because it is absent but because the cue–trace
overlap is zero.

This axiom descends from [[B1-spreading-activation]]: spreading activation only
reaches a node if a cue activates a pathway leading to it; with zero overlap, no
activation arrives. It supports [[B4-index-store-split]] (the index must be built
around anticipated retrieval cues) and [[C2-three-orderings]] (retrievability is a
separate ledger from confidence, and it is cue-contingent).

Evidence: [[tulving-1973-encoding-specificity]].
