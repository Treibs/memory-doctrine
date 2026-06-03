---
id: D3-consolidation-mtt-safe
type: axiom
cluster: D-dynamics
title: Consolidation moves traces toward cortex, but promote-and-keep-indexed — never promote-and-detach
statement: >
  Systems consolidation transfers memory from a fast hippocampal index toward
  durable neocortical storage via offline replay (Wilson & McNaughton 1994), but the
  standard model (full index-independence after consolidation) vs. Multiple-Trace
  Theory (hippocampal index needed for life for episodic detail; Nadel & Moscovitch
  1997) is UNRESOLVED. Safety clause: promotion to the doctrine tier must be
  PROMOTE-AND-KEEP-INDEXED — never promote-and-detach. Detachment builds Alzheimer's
  fragility: the entorhinal/hippocampal index hub degrades first (Braak stages I–II
  are clinically silent), severing access to everything downstream before any
  retrieval symptom appears.
domain: developmental-clinical
generativity: 4
confidence: 0.82
status: locked
relations:
  derives-from: [B4-index-store-split]
  supports: [D4-contract]
  generalizes: []
  contradicts: []
  applies-to-kpm: [consolidation-cron, promote-and-keep-indexed, hub-integrity, replay-pass]
evidence: [wilson-1994-replay, nadel-1997-mtt, braak-1991-staging]
provenance: memory-research/developmental-clinical-deep
verification: {challenged: true, citations_checked: true, gate: "rt3+purge"}
---

# D3 · Consolidation: promote-and-keep-indexed (MTT-safe)

Systems consolidation is the process by which a memory migrates from a fast,
episodic, interference-prone hippocampal store toward durable, schematic, integrated
neocortical storage. Its KPM analogue is the promotion of a provisional `research/`
finding into a stable doctrine-tier axiom. This axiom governs that promotion
operation and grounds it in [[B4-index-store-split]].

## The replay mechanism (Wilson & McNaughton 1994)

Hippocampal place-cell pairs that co-fired during waking experience showed increased
co-firing during subsequent slow-wave sleep — the discovery of **offline replay as
the engine of systems consolidation**. This establishes consolidation as a *scheduled
batch background process*, not a synchronous write. See [[wilson-1994-replay]].

## The unresolved debate: standard model vs. MTT

**Standard model** (Squire & Alvarez 1995; McClelland, McNaughton & O'Reilly 1995):
after sufficient replay the neocortex can retrieve the memory **independently** of
the hippocampal index — the index becomes optional. Confidence in this model gives
D3 the "detach" interpretation.

**Multiple-Trace Theory** (Nadel & Moscovitch 1997, [[nadel-1997-mtt]]): the
hippocampus is required for *all* episodic/contextual detail however remote. What
becomes cortex-independent is a gist/semantic abstraction; the rich episodic original
always needs the hippocampus. Neuroimaging evidence broadly favors MTT (conceded by
Squire & Wixted 2011).

**The debate is genuinely unresolved** — this is why confidence is 0.82, not higher.

## The Braak safety clause

Alzheimer's neurofibrillary degeneration begins invariably in the
**transentorhinal and entorhinal cortex** — the anatomical hub through which all
hippocampo-neocortical traffic routes — then spreads to the hippocampus proper, then
to association neocortex (Braak stages I–VI; see [[braak-1991-staging]]). Stages I–II
are **clinically silent**: the hub is degrading while retrieval appears normal.

**Implication for KPM:** any architecture that "detaches" a promoted axiom from the
index *relies on the hub being intact*. When the hub degrades first and silently, the
detached axiom becomes unretrievable with no early-warning symptom — the exact
failure mode Braak documents. The safety clause is therefore not conservative
caution; it is load-bearing engineering: **if it is safe per MTT, it is safe per the
standard model too; if it would break per MTT, it is not safe to ship**.

## Promote-and-keep-indexed (the safe policy)

```
PROMOTE(axiom a) →
  1. Replicate a to doctrine tier (increase confidence, mark stable)
  2. KEEP the index entry intact — do not remove a from retrieval index
  3. Strengthen index edges (not remove them)
  4. Record provenance: from-research/ + replay-pass timestamp
```

This is MTT-safe: even if the hippocampal-analogue hub of the KPM degrades, the
index pointers still exist. It is also standard-model-compatible: the doctrine tier
can answer without the index if the index is intact — the index is not *needed* for
retrieval but is *present* for recovery.

## KPM implications

- **Consolidation is a scheduled offline cron** (replay-pass), not a synchronous
  write on ingestion. Recent items live in the episodic capture tier (`research/`);
  the cron promotes corroborated ones to the doctrine tier.
- **Hub integrity is the top health-check priority** — the index/meta-axiom layer
  is the entorhinal analogue: it degrades first and silently. `kpm doctor` should
  monitor hub node connectivity as a leading indicator, not a trailing one.
- **Consolidation never removes an axiom from the retrieval index.** Promote-and-detach
  is explicitly forbidden by this axiom until the MTT/standard-model debate is
  resolved in favor of the standard model with strong neuroimaging evidence.
- The [[B4-index-store-split]] is the static architecture; D3 is its *temporal
  dynamics* — how the split evolves as findings mature into doctrine.
- D3 supports [[D4-contract]]: the promote-and-keep-indexed policy means a
  promoted axiom's entrenchment is governed by D4's revision contract, not by
  the consolidation cron.
