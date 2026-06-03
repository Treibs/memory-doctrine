---
id: A2-atomicity
type: axiom
cluster: A-structure
title: One idea per node — atomicity enables composability
statement: >
  Each knowledge node must contain exactly one self-contained idea (Zettelkasten /
  Luhmann; evergreen notes / Matuschak). The rationale is composability, not
  retrieval speed: only an atom can be linked precisely, reused across contexts,
  and addressed as a stable unit. A multi-claim node produces ambiguous links
  and collapses the network's combinatorial power.
domain: pkm-notes
generativity: 4
confidence: 0.85
status: locked
relations:
  derives-from: []
  supports: [C2-three-orderings, F2-contradictions-category-errors]
  generalizes: []
  contradicts: []
  applies-to-kpm: [atomicity-rule, composability, node-design]
evidence: [matuschak-2019-evergreen, luhmann-1981-zettelkasten]
provenance: memory-research/pkm-notes
verification: {challenged: true, citations_checked: true, gate: "rt1+purge"}
---

# A2 · Atomicity — one idea per node

The PKM tradition independently re-derived the same rule from two directions
across 40 years: Luhmann's physical *Zettel* forced a single addressable idea per
card; Matuschak's evergreen-notes canon makes the design principle explicit. Both
arrive at the same conclusion.

**The composability rationale (v1.1 correction):** The atomicity rule is often
stated as benefiting *retrieval*, but the v1.1 purge corrected this: the primary
rationale is **composability**. An atom can be:

- linked precisely (the connection points to one clean idea, not a multi-claim blob)
- reused across contexts without dragging unwanted baggage
- addressed as a stable unit in logical derivations

A multi-claim node produces ambiguous edges. The links connect blurry
multi-meaning objects; the network's combinatorial power collapses because
each link imports several ideas at once, making the graph's semantics
uninterpretable. Composability is the mechanism behind the PKM promise of
*emergent* recombination: atoms-as-concepts recombine into novel insights
precisely because each atom is clean.

**Relation to the KPM schema:** The SPEC's `type: axiom` — one file per axiom —
directly instantiates this rule. A KPM file that asserts two generative claims is
an atomicity violation and should fail the lint. The distinction between the three
orderings ([[C2-three-orderings]]) is itself an atomicity application: three
concepts that *were* conflated as one until the purge separated them.

**Relation to category-errors:** [[F2-contradictions-category-errors]] notes that
most apparent contradictions are category errors — two distinct quantities
conflated into one. Atomicity is the structural prophylactic: clean atoms make
conflation detectable.

**Evidence:** [[matuschak-2019-evergreen]] provides the explicit design-principle
statement with the composability rationale. [[luhmann-1981-zettelkasten]] is the
45-year existence proof that atomic, linked cards compound generatively — ~70 books
and ~400 articles from one slip-box.
