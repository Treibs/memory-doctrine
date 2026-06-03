---
id: C3-confident-but-wrong
type: axiom
cluster: C-truth
title: High confidence does not imply truth — gist compression is mathematically priced error
statement: >
  High confidence is neither necessary nor sufficient for truth. In any
  spreading-activation / gist-based store, confidently-false memories arise
  from normal associative processing: the DRM paradigm shows ~72% of never-
  presented lures are "remembered" with vivid, conscious recollection
  (Roediger & McDermott 1995). The information-theoretic root is that gist
  storage operates below the source entropy H; every bit saved below H incurs
  a formally quantified distortion (Shannon R(D)). Confabulation is not a
  defect — it is the priced cost of compression. Any KPM retrieval layer that
  uses spreading activation or vector interpolation will exhibit this failure
  mode. Mitigation: source-type all retrieved nodes; interpolated "gist" nodes
  are hypotheses and may never inherit a stored, verified node's confidence.
domain: cognitive-psych
generativity: 4
confidence: 0.92
status: locked
relations:
  derives-from: [C1-confidence-earned, B1-spreading-activation, E1-layered-distillation]
  supports: [E4-adversarial-verify, F1-convergence-corroboration, F2-contradictions-category-errors]
  generalizes: []
  contradicts: []
  applies-to-kpm: [source-typed-retrieval, interpolation-hypothesis-flag]
evidence: [roediger-1995-drm, shannon-1959-rate-distortion]
provenance: memory-research/salience-errors-deep
verification: {challenged: true, citations_checked: true, gate: "rt1+purge"}
---

# C3 · Confident-but-wrong — gist compression is priced distortion

A spreading-activation or vector-similarity retrieval layer does not fail by
returning *nothing*. It fails by confidently returning a **plausible interpolation
that was never stored**. This is the dark side of [[B1-spreading-activation]].

**The empirical evidence (DRM paradigm).** Roediger & McDermott (1995) showed that
studying semantic associates of a critical lure (e.g., words related to "sleep")
produces false recall at ~55% — statistically indistinguishable from true recall —
and, crucially, ~72% of falsely-*recognized* lures received "Remember" judgments:
vivid, phenomenologically confident, conscious recollection of a word never
presented. This is not low-confidence guessing; it is maximum-confidence
confabulation from a system working exactly as designed. Deese (1959) established
the precursor: critical-lure intrusions up to ~44% in free recall.

**The mathematical root.** Shannon (1959) established the rate-distortion function
R(D): below the source entropy H, lossless reconstruction is impossible. Every bit
saved below H incurs a quantified, mandatory distortion. When a memory system (or
KPM retrieval layer) stores gist rather than verbatim traces, it is operating at
D > 0 on the R(D) curve. The resulting errors are not random noise — they are
statistically structured interpolations toward the centroid of the compressed
manifold. This is precisely the mechanism the DRM paradigm reveals. E1's
"distill the generator" move is *not* lossy — it strips recoverable redundancy
above H, preserving the irreducible core — but any additional compression or
interpolation crosses the line into priced error. This is the formal mathematical
grounding of C3, noted explicitly in the v1.1 spine.

**KPM consequence.** Any retrieval layer that:
- does vector-embedding similarity search (cosine interpolation)
- does multi-hop spreading activation
- does GraphRAG-style subgraph completion

will produce C3-style confabulations. The mitigation is **source-typed retrieval**:

| Node type | Source tag | Permitted to inherit stored confidence? |
|---|---|---|
| Directly stored, cited axiom | `verified-stored` | Yes |
| Inferred by spreading activation | `inferred` | No — hypothesis only |
| Vector-interpolated | `interpolated` | No — hypothesis only |
| Derived by KPM chain | `derived` | Yes, up to the min-confidence of the chain |

`kpm doctor` must FAIL if an `inferred` or `interpolated` node carries a
`confidence` value without a separate `inference-confidence` tag and a note that it
is a hypothesis.

This axiom derives from [[C1-confidence-earned]] (the baseline that confidence is
earned, not asserted) and [[B1-spreading-activation]] (the retrieval mechanism
whose dark side this is), and [[E1-layered-distillation]] (whose Shannon grounding
provides the mathematical root). It supports [[E4-adversarial-verify]] (the
adversarial check is the primary defence against C3 confabulation) and
[[F1-convergence-corroboration]] (convergence is required precisely because any
single spreading-activation path may confabulate). C3 confabulations are a primary
instance of [[F2-contradictions-category-errors]]: a high-confidence interpolation
colliding with a stored verified node is a category error, not a mere disagreement.

Evidence: [[roediger-1995-drm]], [[shannon-1959-rate-distortion]].
