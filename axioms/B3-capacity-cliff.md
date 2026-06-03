---
id: B3-capacity-cliff
type: axiom
cluster: B-retrieval
title: Associative stores have a sharp capacity cliff — shard, don't cram
statement: >
  Classical Hopfield networks black out entirely above ≈0.138N stored patterns (Amit,
  Gutfreund & Sompolinsky 1985); this is a cliff, not a graceful slope. Modern
  continuous-Hopfield networks escape via softmax to exponential capacity, but the
  all-or-none ignition threshold remains — matching global-workspace theory's
  capacity-bounded broadcast. Implication: keep knowledge packages small and sharded.
domain: computational-models
generativity: 4
confidence: 0.88
status: locked
relations:
  derives-from: [B1-spreading-activation]
  supports: [E1-layered-distillation]
  generalizes: []
  contradicts: []
  applies-to-kpm: [package-sizing, shard-strategy]
evidence: [amit-1985-capacity-cliff, ramsauer-2020-hopfield]
provenance: memory-research/semantic-networks
verification: {challenged: true, citations_checked: true, gate: "rt1+purge"}
---

# B3 · Associative stores have a sharp capacity cliff — shard, don't cram

Classical Hopfield networks exhibit a **phase transition**: below ≈0.138N patterns
the network retrieves correctly; above it, retrieval collapses catastrophically — not
gracefully. This is the Amit–Gutfreund–Sompolinsky result (full replica derivation,
*Physical Review Letters* 55:1530, 1985; *Annals of Physics* 173, 1987). The capacity
is a cliff, not a slope.

Modern continuous-Hopfield networks (exponential in N — see [[ramsauer-2020-hopfield]])
escape the hard 0.138N ceiling by replacing binary states with continuous activations
and softmax retrieval. But even modern Hopfield retains an **all-or-none ignition
dynamic**: the softmax concentrates all weight on one retrieved pattern (low
temperature) or diffuses across many (high temperature). This maps directly onto
global-workspace theory's capacity-bounded broadcast: only what achieves ignition
(crosses the softmax threshold) reaches the workspace; everything else stays
sub-threshold.

The engineering consequence is unambiguous: do not cram a single associative store
with unbounded content. Past the cliff, you retrieve nothing specific — the system
hallucinates attractors rather than stored patterns. **Shard packages; keep each store
well within safe capacity.** The sharding itself (small, typed, pruned KPMs) is
supported by [[E1-layered-distillation]] as the distillation pattern that keeps each
package coherent and retrievable.

This axiom derives from [[B1-spreading-activation]] (capacity constrains how many
attractors an energy-descent retrieval can reliably serve).

Evidence: [[amit-1985-capacity-cliff]], [[ramsauer-2020-hopfield]].
