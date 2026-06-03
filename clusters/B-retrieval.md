---
id: B-retrieval
type: cluster
title: B · Retrieval — how knowledge is recalled
---

# B · Retrieval

Retrieval is not lookup — it is energy-descent pattern completion over a content-addressable store, and its rigorous form (the modern Hopfield update) is mathematically identical to transformer attention. Because recall is a join between encoding context and retrieval cue, effective memory requires indexing for the anticipated question, not adding more aliases. Associative capacity is a hard cliff — not a graceful slope — so packages must stay sparse and sharded. The architectural consequence is a clean split between a sparse index (the KPM's axiom graph) and a rich evidence store, a separation proven both computationally (catastrophic interference) and biologically (hippocampal indexing theory).

Axioms: [[B1-spreading-activation]], [[B2-cue-dependence]], [[B3-capacity-cliff]], [[B4-index-store-split]].
