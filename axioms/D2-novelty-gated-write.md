---
id: D2-novelty-gated-write
type: axiom
cluster: D-dynamics
title: Write-on-retrieval is gated by prediction error — reconsolidation labilizes only under mismatch
statement: >
  Retrieval re-opens a memory trace (reconsolidation), but destabilization occurs
  ONLY when retrieval carries a prediction error / mismatch (Sevenster & Kindt 2013).
  Pure re-confirmation reinforces retrievability without labilizing the trace; a
  mismatch triggers labilization → integration of new evidence → re-stabilization.
  Three-zone policy: no-PE → reinforce retrievability only; moderate-PE →
  reconsolidate and integrate into the existing node; large/sustained-PE → mint a
  NEW node (do not overwrite). Note: one failed replication exists (2022) — boundary
  conditions on reconsolidation are real but fragile.
domain: engram-consolidation
generativity: 5
confidence: 0.85
status: locked
relations:
  derives-from: [D1-retrievability-decay]
  supports: [F3-surprise-principle]
  generalizes: []
  contradicts: []
  applies-to-kpm: [write-on-retrieval, prediction-error-gate, node-vs-update-policy]
evidence: [sevenster-2013-reconsolidation, nader-2000-reconsolidation]
provenance: memory-research/engram-consolidation-deep
verification: {challenged: true, citations_checked: true, gate: "rt3+purge"}
---

# D2 · Novelty-gated write-on-retrieval

Retrieval is not a passive read — it re-opens the write window. But the window only
**does anything** when the retrieval carries a prediction error. This connects to
[[F3-surprise-principle]]: prediction error is ONE quantity doing the work of three
(behavioral/dopaminergic/cortical), and reconsolidation is its memory-write
instantiation. It also follows on from the retrievability/confidence split in
[[D1-retrievability-decay]]: retrieval without surprise strengthens retrievability
only, not confidence.

## The prediction-error gate (Sevenster & Kindt 2013)

Sevenster, Kindt and colleagues showed that **retrieval in the absence of prediction
error does NOT destabilize a consolidated memory** — the trace remains stable and
anisomycin (protein synthesis inhibitor) has no amnesic effect. Only when retrieval
is accompanied by a violation of expectation does the trace enter a labile state
requiring re-stabilization. See [[sevenster-2013-reconsolidation]].

One failed replication was reported in 2022 — reconsolidation boundary conditions
are real phenomena but their parametric sensitivity is not fully mapped. Confidence
is therefore 0.85, not higher.

## Reconsolidation mechanics (Nader 2000)

The underlying mechanism was established by Nader, Schafe & LeDoux (2000): a
consolidated fear memory infused post-retrieval with a protein synthesis inhibitor
showed retrograde amnesia — proving the retrieved trace re-entered a labile,
protein-synthesis-dependent state. Without retrieval the same infusion left the
memory intact. See [[nader-2000-reconsolidation]].

## Three-zone write policy

| Prediction-error magnitude | KPM action |
|---|---|
| No PE (pure re-confirmation) | Reinforce `retrievability` only; no trace change |
| Moderate PE (new info extends / conflicts with existing node) | Reconsolidate: integrate new evidence into the existing axiom node; re-score confidence; re-stabilize |
| Large / sustained PE (fundamental mismatch, new domain) | Mint a NEW axiom node — do NOT overwrite the existing one; link with `contradicts` or `supersedes` edge |

## KPM implications

- **Don't re-write on every retrieval.** Re-write only when there is a detectable
  mismatch: new evidence conflicts with or meaningfully extends the axiom.
- Re-confirmation during a cold retrieval (high-difficulty recall) bumps
  `retrievability` — the exact quantity [[D1-retrievability-decay]] tracks.
- The "large PE → new node" rule prevents overwriting good existing axioms with
  conflicting new findings; it gives the F2 "split when conflated" operation its
  write-side trigger.
- Integration at the axiom level must pass E4 adversarial verification before
  re-stabilization is committed (the same plasticity window is a false-memory vector,
  per the engram research).
