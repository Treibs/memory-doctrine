---
id: B1-spreading-activation
type: axiom
cluster: B-retrieval
title: Spreading activation is Hopfield is attention
statement: >
  Retrieval is energy-descent pattern completion over a content-addressable
  store; the modern continuous-Hopfield update is mathematically identical to
  transformer attention (xi_new = X softmax(beta X^T xi)).
domain: semantic-networks
generativity: 5
confidence: 0.95
status: locked
relations:
  derives-from: [A1-fan-budgeted-edges]
  supports: [B4-index-store-split]
  generalizes: []
  contradicts: []
  applies-to-kpm: [recall-mechanism]
evidence: [ramsauer-2020-hopfield, hopfield-1982]
provenance: memory-research/semantic-networks
verification: {challenged: true, citations_checked: true, gate: "rt1+purge"}
---

# B1 · Spreading activation ≡ Hopfield ≡ attention

Retrieval is not lookup; it is energy-descent pattern completion. The modern
Hopfield network's one-step update is identical to attention, so an embedding
store *is* an associative memory. This grounds [[B4-index-store-split]] and
descends from [[A1-fan-budgeted-edges]].

Evidence: [[ramsauer-2020-hopfield]], [[hopfield-1982]].
