---
id: F2-contradictions-category-errors
type: axiom
cluster: F-meta
title: Apparent contradictions are usually category errors — split or merge
statement: >
  When two well-evidenced claims appear to contradict, the most productive move
  is to suspect a conflated term: split the term into two distinct concepts and
  both halves will typically be true (e.g., confidence vs. retrievability; edge
  count vs. signal-per-fan). The twin rule is equally important: when three
  separately-named findings share one underlying computational generator, merge
  them under that generator rather than maintaining parallel machinery.
domain: epistemology
generativity: 5
confidence: 0.90
status: locked
relations:
  derives-from: [A3-foundherentist-generativity]
  supports: [C2-three-orderings, F3-surprise-principle]
  generalizes: []
  contradicts: []
  applies-to-kpm: [contradiction-resolution, concept-hygiene]
evidence: [haack-1993-foundherentism, quine-1951-two-dogmas]
provenance: memory-research/epistemology
verification: {challenged: true, citations_checked: true, gate: "rt1+purge"}
---

# F2 · Apparent contradictions are usually category errors — split or merge

**The split rule.** When two well-supported claims appear to contradict, assume a
conflated concept before assuming a genuine inconsistency. The doctrine resolved every
one of its v0 contradictions this way:

- M5 vs. M6 appeared to contradict ("memory strengthened by use" vs. "memory fades
  with disuse"): the term *memory strength* was conflated. Split into *evidential
  confidence* (raised only by new evidence) and *retrievability* (decays with disuse,
  restored by retrieval) → [[C2-three-orderings]]. Both halves are true.
- "Orphan nodes = worthless" vs. "more connections = richer memory" appeared to
  contradict: *edge count* was conflated with *signal-per-fan*. Adding a low-signal
  edge dilutes all others (ACT-R fan law). Both halves true after the split.
- Foundationalism vs. coherentism appeared to contradict: *justification structure*
  was conflated. Foundherentism (Haack; [[haack-1993-foundherentism]]) shows they are
  the vertical axis (foundation → derived) and the horizontal axis (mutual support) of
  the same object. Quine's web ([[quine-1951-two-dogmas]]) reconciles them concentrically.

**The merge rule (the twin, added in v1.1).** Equally important: when three
separately-named mechanisms share one computational generator, maintaining them as
parallel machinery is the *over-split* error. The Surprise Principle ([[F3-surprise-principle]])
is the doctrine's canonical merge case: C4 (salience-gating), D2 (novelty-gated write),
and predictive coding are the *same* quantity — prediction error — at three levels of
description. They should be unified under one generator, not maintained as three
separate provisions.

**The diagnostic heuristic (F2 meta-rule):**
1. Two claims in tension → enumerate which term they share → check if the term
   carries two distinct meanings → split. Both halves become axioms with a
   `generalizes` relation pointing to the original conflated node.
2. Three claims that converge → check if they share one mathematical or
   computational generator → merge. The merged node becomes the new axiom;
   the three become evidence nodes or `applies-to` instances.

This principle descends from [[A3-foundherentist-generativity]]: the crossword analogy
(mutual coherent support) only works when the squares are correctly individuated. Wrong
individuations produce apparent contradictions that dissolve on closer analysis.
