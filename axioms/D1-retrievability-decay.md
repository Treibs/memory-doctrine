---
id: D1-retrievability-decay
type: axiom
cluster: D-dynamics
title: Retrievability drops from disuse, competition, and deliberate intent — confidence does not
statement: >
  Retrievability decays from THREE independent drivers: (1) disuse — power-law decay
  toward a floor (Ebbinghaus/Wixted 1991); (2) competition — retrieval-induced
  forgetting (Anderson 1994), cue-independent, driven by practice strengthening one
  trace at the expense of unpracticed neighbors; (3) deliberate intent — directed
  forgetting (Bjork 1989), an active suppression process distinct from passive decay.
  Evidential confidence does NOT decay from any of these; it changes only on new
  evidence (Bjork two-strengths: storage strength vs. retrieval strength). A decayed
  axiom is DORMANT, not doubted.
domain: forgetting-consolidation
generativity: 5
confidence: 0.92
status: locked
relations:
  derives-from: [C2-three-orderings]
  supports: [D2-novelty-gated-write, D5-suppress]
  generalizes: []
  contradicts: []
  applies-to-kpm: [retrievability-score, decay-job, dormant-not-doubted]
evidence: [bjork-1992-two-strengths, anderson-1994-rif, bjork-1989-directed-forgetting]
provenance: memory-research/forgetting-consolidation
verification: {challenged: true, citations_checked: true, gate: "rt3+purge"}
---

# D1 · Retrievability decays from three drivers — confidence does not

Retrievability and evidential confidence are **two distinct scores** on an axiom
([[C2-three-orderings]]). This axiom governs the retrievability dimension only.

## The three drivers of retrievability loss

**Driver 1 — Disuse (power-law decay).** Ebbinghaus established the forgetting curve;
Wixted & Ebbesen (1991) formalized its shape as a power function `R = a·t^(−b)`:
the instantaneous decay rate *slows* as a memory ages — old memories are more stable
per unit time than young ones (Jost's law). Floor is approached but never hit from
time alone. See [[bjork-1992-two-strengths]] for the storage-vs-retrieval split that
explains why this affects only retrieval strength.

**Driver 2 — Competition (retrieval-induced forgetting, RIF).** Anderson (1994)
demonstrated that practicing a subset of items from a category *actively suppresses*
the retrieval strength of unpracticed neighbors. This is **cue-independent** — it is
not mere fan competition (A1's budget effect) but an executive inhibitory process
that applies even when the cue does not directly activate the competing trace. See
[[anderson-1994-rif]].

**Driver 3 — Deliberate intent (directed forgetting).** Bjork (1989) showed that
intentional instructions to forget produce *different* and stronger forgetting than
passive decay — a process distinct from interference and from disuse, involving
active suppression of encoding or retrieval routes. See
[[bjork-1989-directed-forgetting]]. Note: D5-suppress is the KPM operator that
formalizes deliberate retrieval suppression; it must be reversible and audit-visible
(see [[D5-suppress]]).

## Confidence is orthogonal

Per Bjork & Bjork's New Theory of Disuse ([[bjork-1992-two-strengths]]):
**storage/evidential strength never decays from disuse — it changes only when new
evidence is added or a defeater lands.** A long-dormant axiom is *not* a doubted
axiom. The decay job touches `retrievability` only; `confidence` requires a
separate evidence-gated operation (C1, C2).

## KPM implications

- A KPM must maintain **two separate scores per axiom**: `retrievability` (volatile,
  decays power-law, snaps back on successful retrieval) and `confidence`
  (evidence-gated, does not decay from disuse).
- The decay job runs on `retrievability` only; cold axioms become dormant (low
  retrievability) not retracted (low confidence).
- Near-duplicate axioms compete via Driver 2 (RIF) — a KPM must dedup/merge
  cue-collision pairs to prevent mutual suppression.
- Driver 3 (directed forgetting / D5) is a first-class write operation, not a
  side-effect — it requires a goal-bound controller and audit trail per [[D5-suppress]].
- Retrievability loss from disuse is the precondition for [[D2-novelty-gated-write]]'s
  gate: retrieval re-opens a trace only if prediction error is present, meaning a
  low-retrievability (dormant) axiom that is successfully cued already carries a
  non-zero PE signal sufficient to trigger reconsolidation.
