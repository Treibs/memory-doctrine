---
id: A3-foundherentist-generativity
type: axiom
cluster: A-structure
title: Justification is foundherentist; generativity equals AGM epistemic entrenchment
statement: >
  A KPM's justification structure is foundherentist (Haack 1993): foundational
  roots supply non-circular grounding while coherentist mutual support amplifies
  justification across the graph — neither pure foundationalism nor pure
  coherentism alone. Generativity is operationally identical to AGM epistemic
  entrenchment: the ordering that determines which belief a rational agent
  surrenders last when forced to contract. High-generativity axioms are the
  protected core; low-generativity findings are the revisable periphery.
domain: epistemology
generativity: 5
confidence: 0.88
status: locked
relations:
  derives-from: []
  supports: [C1-confidence-earned, C2-three-orderings, D3-consolidation-mtt-safe, E4-adversarial-verify]
  generalizes: []
  contradicts: []
  applies-to-kpm: [justification-structure, generativity-field, belief-revision, revision-policy]
evidence: [haack-1993-foundherentism, agm-1985-belief-revision]
provenance: memory-research/epistemology
verification: {challenged: true, citations_checked: true, gate: "rt1+purge"}
---

# A3 · Foundherentist justification — generativity = AGM entrenchment

The doctrine's epistemological spine is a v0 correction: M11 in the original beat
mis-attributed the foundationalist structure to Quine (a *holist* with no immune
core). The corrected position is **foundherentism** (Haack 1993).

## The foundherentist structure

Pure foundationalism fails: it requires a justification-immune base that cannot
itself be questioned, which is both philosophically untenable and practically
fragile. Pure coherentism fails: a coherent fairy-tale can be internally
consistent yet false (the isolation objection). Haack's **crossword analogy**
resolves both:

- *Horizontal* (across entries) = coherentist mutual support: axioms constrain
  and reinforce each other; a tightly connected cluster raises the justified
  confidence of all its members.
- *Vertical* (entries anchored to clues) = foundational grounding: some axioms
  are directly anchored to external evidence, providing non-circular warrant.

The KPM's schema instantiates both dimensions: the `evidence` field (required on
every axiom) is the vertical anchor; the `derives-from` / `supports` / `generalizes`
edges are the horizontal coherence web. An axiom with empty evidence is an
unanchored node; a disconnected axiom is coherentially bankrupt. Both are KPM
defects.

## Generativity as AGM epistemic entrenchment

The formal machinery for "which axiom do you surrender last?" already exists: AGM
**epistemic entrenchment** (Alchourrón, Gärdenfors & Makinson 1985;
Gärdenfors & Makinson 1988). The entrenchment ordering `≤` satisfies:

- **Transitivity**: if `p ≤ q` and `q ≤ r` then `p ≤ r`.
- **Dominance**: if `p ⊢ q` then `p ≤ q` — logically stronger / more specific
  beliefs are less entrenched than their generators.
- **Minimality**: non-believed propositions are least entrenched.
- **Maximality**: tautologies (the most general truths) are maximally entrenched.

The contraction rule reads directly off entrenchment: when forced to give
something up, surrender the *least entrenched* belief in the conflicting set.
The KPM's `generativity: 1–5` field IS this ordering — made operational.
Dominance confirms the doctrine's core claim: derived findings (more specific,
more dependent) are naturally less entrenched than their generators. Revise
periphery first; touch a `gen=5` root only under strong multi-source evidence.

## Quine's role (corrected)

Quine's web of belief (holism, "Two Dogmas" 1951) is consistent with
foundherentism but is not the justification for it. Quine shows that no belief
is immune from revision in principle — even the most central ones can be
revised at high enough evidential cost. This is fully compatible with
foundherentism: Haack's roots are *more resistant*, not *immune*.
Quine's holism is the boundary condition, not the architecture.

## Relations to other axioms

The foundherentist structure explains *why* [[C1-confidence-earned]] is
non-negotiable: only evidence can raise confidence because the crossword's
vertical anchors are the sole source of non-circular grounding — fluency,
recency, or frequency of retrieval cannot substitute. It grounds the three-way
separation in [[C2-three-orderings]]: entrenchment (= generativity) is a
distinct ordering from confidence and from retrievability, and conflating any
two collapses the justification structure. It also underlies [[D3-consolidation-mtt-safe]]
(promote-and-keep-indexed preserves the crossword's both dimensions) and
[[E4-adversarial-verify]] (independent security = the crossword's horizontal
check, the anti-Gettier guardrail).

**Evidence:** [[haack-1993-foundherentism]] establishes the foundherentist
position and the crossword analogy with its warrant calculus.
[[agm-1985-belief-revision]] formalizes epistemic entrenchment and the
rationality postulates that make the `generativity` field operationally precise.
