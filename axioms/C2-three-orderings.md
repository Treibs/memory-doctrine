---
id: C2-three-orderings
type: axiom
cluster: C-truth
title: Three independent orderings that must never be collapsed
statement: >
  Every axiom in a KPM sits on three INDEPENDENT orderings that must never be
  conflated: (1) generativity / entrenchment — how much downstream structure
  derives from it and how reluctantly it is surrendered (Quine/AGM); (2)
  confidence — the evidence-earned credence that changes only on new evidence
  (C1); (3) retrievability — the volatile activation level that decays with disuse
  and is restored by retrieval (D1). Collapsing any two is a category error that
  will corrupt both the write-policy and the read-policy of the KPM.
domain: epistemology
generativity: 5
confidence: 0.93
status: locked
relations:
  derives-from: [C1-confidence-earned, A3-foundherentist-generativity, D1-retrievability-decay]
  supports: [D4-contract, D5-suppress, E3-lint, F2-contradictions-category-errors]
  generalizes: []
  contradicts: []
  applies-to-kpm: [score-separation, kpm-doctor-score-lint]
evidence: [bjork-1992-two-strengths, quine-1951-two-dogmas]
provenance: memory-research/epistemology
verification: {challenged: true, citations_checked: true, gate: "rt1+purge"}
---

# C2 · Three independent orderings — the two/three-score firewall

A KPM node is characterized by at least three properties that look similar but
measure completely different things:

| Ordering | What it measures | Changes when | Operator |
|---|---|---|---|
| **generativity** (entrenchment) | How much downstream content derives from this axiom; how reluctantly it is surrendered | A better generator emerges or the axiom is refuted at root | `D4-contract` |
| **confidence** | Evidence-earned credence; strength of the epistemic case | New confirming or disconfirming evidence arrives | `C1-confidence-earned` |
| **retrievability** | Volatile activation level; how easily cued right now | Disuse (decays), retrieval (restored), `D5-suppress` | `D1-retrievability-decay` |

**Why this matters (the category errors):**

*Confidence ≠ generativity.* A highly generative (core, web-central) axiom can be
poorly evidenced; a peripheral observation can be extremely well-evidenced. Quine's
web-of-belief shows generativity is *radial position* — revised last — not
*confidence level* — revised when evidence demands. Conflating them produces the
error of protecting a high-generativity belief from evidence updates, or conversely,
of trying to "earn" generativity through citation volume rather than through
downstream derivations. AGM entrenchment is a *revision-order* quantity, not a
probabilistic degree-of-belief.

*Confidence ≠ retrievability.* Bjork & Bjork (1992) showed storage strength (≈
evidential confidence) and retrieval strength (≈ retrievability) are dissociable:
storage strength never decays from disuse, only retrieval strength does. A dormant,
rarely-retrieved axiom may be excellently evidenced (high confidence) but hard to
cue (low retrievability). The `D5-suppress` operator deliberately lowers
retrievability without touching confidence — a legal operation precisely because the
two are separate ledgers.

*Generativity ≠ retrievability.* A high-generativity axiom that is poorly indexed
(few incoming cue edges) may be retrieved rarely. Its importance to the doctrine is
not diminished by low activation; its activation is not increased by its importance.
ARC caching (recency + frequency) is the right model for retrievability; it is the
*wrong* model for confidence or generativity.

`kpm doctor` must assert the three are independently maintained:
- FAIL if a `suppress` op touched `confidence`.
- FAIL if a decay event touched `confidence`.
- FAIL if `generativity` was inferred from `confidence` or vice-versa.
- WARN if `generativity` and `confidence` are perfectly rank-correlated across a
  package (suggests they are being set from the same source, i.e. conflated).

Derives from [[C1-confidence-earned]], [[A3-foundherentist-generativity]], and
[[D1-retrievability-decay]] (the third ordering). Supports the separation enforced
by [[D4-contract]] and [[D5-suppress]] operators and the [[E3-lint]] pass.
Collapsing any two orderings is a category error in the sense of
[[F2-contradictions-category-errors]]: treating confidence as retrievability (or
either as generativity) produces a structurally different kind of mistake — not
a disagreement to resolve by evidence but a conceptual mis-mapping to correct by
re-categorisation.

Evidence: [[bjork-1992-two-strengths]], [[quine-1951-two-dogmas]].
