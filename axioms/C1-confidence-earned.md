---
id: C1-confidence-earned
type: axiom
cluster: C-truth
title: Confidence is earned by evidence and is revisable
statement: >
  Confidence is a credence — a graded degree of belief that must be earned by
  verified external evidence and revised by conditionalization on new evidence.
  It must never be inferred from fluency, recency, embedding-similarity,
  salience, retrieval-frequency, or how many (non-independent) supporting
  edges a node has. Confidence is the meta-level score; it changes only when
  evidence changes — not when a belief is retrieved more often.
domain: epistemology
generativity: 5
confidence: 0.92
status: locked
relations:
  derives-from: [A3-foundherentist-generativity]
  supports: [C2-three-orderings, C3-confident-but-wrong, C4-salience-gating, F1-convergence-corroboration, E4-adversarial-verify]
  generalizes: []
  contradicts: []
  applies-to-kpm: [confidence-field, kpm-doctor-confidence-lint]
evidence: [ramsey-1926-credence, koriat-1993-accessibility, gettier-1963-jtb]
provenance: memory-research/epistemology
verification: {challenged: true, citations_checked: true, gate: "rt1+purge"}
---

# C1 · Confidence is earned by evidence and is revisable

Confidence in a KPM node is a **credence** — a degree of belief — that must be
set and updated exclusively by verified external evidence, following the Bayesian
conditionalization rule (Ramsey: P_new(H) = P_old(H | E)). This is formalized
in SPEC's `confidence: 0.0–1.0` field.

The field must be insulated from every *in-band* fluency cue the memory system
would naturally generate: retrieval frequency, embedding similarity, recency of
access, salience/arousal, or the volume of (mutually-dependent) supporting edges.
Koriat (1993) showed that the human feeling-of-knowing is computed from exactly
these cues — counting correct *and incorrect* accessible information alike — making
it systematically miscalibrated. A KPM that lets its own retrieval statistics set
confidence will replicate the human illusion of competence at machine speed.

The Gettier counterexamples add a second guardrail: justification (confidence)
can be fully present yet fail to constitute knowledge, because the truth was reached
by luck rather than a reliable process. High confidence therefore never certifies
correctness on its own; the `provenance` and `verification` fields are the
**anti-Gettier layer** — tracking *how* the belief was reached, not just whether it
has citations.

Practical consequences for `kpm doctor`:
- FAIL if `confidence` correlates with retrieval frequency, fluency, or recency.
- FAIL if a high-confidence axiom has empty `evidence` (Gettier risk — luckily-
  true-but-ungrounded).
- FAIL if `confidence` was lowered *only* due to disuse without new disconfirming
  evidence (that is D1's retrievability decay, not C1's domain).

This axiom supports [[C2-three-orderings]] (confidence is one of the three
independent orderings), [[C3-confident-but-wrong]] (the failure mode when
fluency corrupts confidence), and [[C4-salience-gating]] (salience must not
touch confidence). It depends on [[A3-foundherentist-generativity]] for the
foundherentist picture of evidential grounding. Corroboration from independent
sources is tracked by [[F1-convergence-corroboration]], which is the primary
mechanism for earning high confidence. [[E4-adversarial-verify]] is the
enforcement layer that confirms confidence has not been inflated by fluency or
citation volume.

Evidence: [[ramsey-1926-credence]], [[koriat-1993-accessibility]], [[gettier-1963-jtb]].
