---
id: F3-surprise-principle
type: axiom
cluster: F-meta
title: Prediction error is one quantity at three levels — the Surprise Principle
statement: >
  Prediction error (the signed mismatch between what was predicted and what
  occurred) is ONE computational quantity doing the work of three separately-named
  mechanisms: the behavioral Rescorla–Wagner surprise term (λ − ΣV), the
  dopaminergic reward prediction error (δ(t); Schultz–Dayan–Montague 1997), and
  the cortical predictive-coding residual. This unifies C4 (salience-gating),
  D2 (novelty-gated write-on-retrieval), and predictive coding under a single
  generator. Three-zone write policy: δ ≈ 0 → reinforce retrievability only;
  moderate δ → reconsolidate/integrate into the node; large/sustained δ → mint
  a NEW node (never overwrite).
domain: reinforcement-learning
generativity: 5
confidence: 0.88
status: locked
relations:
  derives-from: [A3-foundherentist-generativity, F2-contradictions-category-errors]
  supports: [D2-novelty-gated-write, C4-salience-gating, D3-consolidation-mtt-safe]
  generalizes: [C4-salience-gating, D2-novelty-gated-write]
  contradicts: []
  applies-to-kpm: [write-gate, promotion-score, three-zone-policy]
evidence: [rescorla-1972-prediction-error, schultz-1997-dopamine-rpe, sevenster-2013-reconsolidation]
provenance: memory-research/reinforcement-learning-deep
verification: {challenged: true, citations_checked: true, gate: "rt1+purge"}
---

# F3 · Prediction error is one quantity at three levels — the Surprise Principle

**The synthesis.** The doctrine v1 named three separate provisions:
- [[C4-salience-gating]]: arousal/importance buys consolidation (promotion score,
  orthogonal to confidence)
- [[D2-novelty-gated-write]]: retrieval re-opens the memory trace only if
  prediction error is present (Nader 2000)
- Predictive coding: cortex broadcasts only the residual between prediction and input

The reinforcement-learning beat
shows these are **the same computational quantity at three levels of description** —
not three independent mechanisms:

| Level | Name | Formalization |
|-------|------|---------------|
| Behavioral | Rescorla–Wagner surprise | `(λ − ΣV)` — evidence: [[rescorla-1972-prediction-error]] |
| Neural broadcast | Dopamine RPE | `δ(t) = r(t) + γV̂(t+1) − V̂(t)` — evidence: [[schultz-1997-dopamine-rpe]] |
| Memory gate | Reconsolidation boundary | PE-gated destabilization — evidence: [[sevenster-2013-reconsolidation]] |

All three are signed prediction error. The Rescorla–Wagner equation `ΔV = αβ(λ − ΣV)`
shows learning stops when the world is fully predicted (ΣV = λ), regardless of
continued contiguity — error, not co-occurrence, is the currency. The dopamine neuron
is the physical instantiation of δ(t) (Schultz, Dayan & Montague 1997 — theory met
electrode; this is F1-grade convergence). Sevenster & Kindt (2013) demonstrated
*causally* (with propranolol) that no prediction error → no memory destabilization →
no update, even under repeated retrieval.

**Honesty clause.** "Same computational quantity" means structurally equivalent, not
identical machinery. Sevenster–Kindt has one failed replication (2022) — the PE-gate
boundary conditions for reconsolidation are real but fragile, especially for
non-fear memories. Confidence 0.88 reflects this (not 0.95+).

**Three-zone write policy (F3 operational form):**

1. **δ ≈ 0** (re-confirmation — new evidence fully matches the axiom's current
   generator + scores): reinforce *retrievability* only; no content edit. This is
   [[D2-novelty-gated-write]]'s "confirmation" case and grounds [[D3-consolidation-mtt-safe]]'s
   distinction between replay (retrievability boost) and content revision.

2. **Moderate δ** (evidence partially mismatches): destabilize the trace; integrate
   the new evidence; re-score Bel/Pl; re-stabilize. This is reconsolidation proper —
   the only window in which an existing axiom's *content* may be revised in-place.

3. **Large/sustained δ** (evidence strongly conflicts with the axiom): do **not**
   overwrite; mint a **new** axiom node and attach a `contradicts`/`supersedes` edge.
   Overwriting at large δ corrupts a well-founded node with an outlier; the "new
   learning" regime creates a distinct trace.

**One signal, two consumers (RL6 grounding):** The same δ that gates content-write
([[D2-novelty-gated-write]]) also gates promotion ([[C4-salience-gating]]). Derive
both from one prediction-error number and consume them differently — fewer moving
parts, biologically licensed (Schultz–Dayan–Montague 1997 "dual roles").

This is the doctrine's canonical example of [[F2-contradictions-category-errors]]'s
*merge* rule: three separately-named provisions (C4, D2, predictive coding) are
unified under one generator. [[F2-contradictions-category-errors]] provides the
meta-move; F3 is its primary instance in the doctrine. The unification itself
instantiates [[A3-foundherentist-generativity]]: one generator (prediction error)
replaces three surface provisions without losing evidential grounding.
