---
id: A1-fan-budgeted-edges
type: axiom
cluster: A-structure
title: Memory value lives in fan-budgeted, weighted edges
statement: >
  A node's retrieval budget is finite and is divided logarithmically among its
  associations: Sij = S − ln(fanj). Adding a low-signal edge provably dilutes
  retrieval of all others. Maximize signal-per-edge, not edge count;
  orphan nodes are near-worthless, indiscriminately-linked nodes are worse.
domain: semantic-networks
generativity: 5
confidence: 0.90
status: locked
relations:
  derives-from: []
  supports: [B1-spreading-activation]
  generalizes: []
  contradicts: []
  applies-to-kpm: [graph-structure, edge-budget, fan-law]
evidence: [anderson-1974-fan, anderson-1993-actr]
provenance: memory-research/semantic-networks
verification: {challenged: true, citations_checked: true, gate: "rt1+purge"}
---

# A1 · Fan-budgeted edges — value is in the edges, not the nodes

Meaning is positional: a node's value is constituted entirely by its pattern of
connections to other nodes (Quillian 1968). But connections carry a cost: each
additional fan member dilutes the activation every other link receives.
Anderson's 1974 fan-effect experiment established this empirically; the ACT-R
formalization gives it exact form:

```
Sij = S − ln(fanj)
```

where `Sij` is the associative strength from context element j to chunk i,
`fanj` is j's fan count, and S is the maximum possible associative strength.
The law is **logarithmic, not linear** — activation is not split 1/n — a
critical v1.1 correction. Doubling the fan costs less than halving strength,
but every additional edge still carries a measurable retrieval penalty on all
existing edges.

**Engineering consequence:** Sparse, high-signal edges outperform dense,
indiscriminate linking. An axiom with no relations is nearly meaningless; an
axiom connected to everything retrieves nothing specifically. Every edge must
earn its place: it earns its place iff it changes what is retrieved on a path
a consumer actually traverses *and* beats its marginal fan cost.

**Relation to retrieval:** This axiom is the structural ancestor of
[[B1-spreading-activation]]: the Hopfield/attention retrieval mechanism
distributes activation along the very edges whose budgets A1 constrains.
The architecture of retrieval (B1) assumes that the graph it operates on
obeys the fan budget law (A1).

**Evidence:** [[anderson-1974-fan]] establishes the empirical fan effect.
[[anderson-1993-actr]] formalizes the logarithmic law `Sij = S − ln(fanj)`
in the ACT-R 2.0 architecture.
