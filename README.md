---
id: README
type: spine
title: The Memory Doctrine
---

# The Memory Doctrine

*A retrieval-optimized, confidence-weighted axiom-set for how knowledge should be shaped, stored, recalled, and revised.*

## The model

Memory is a retrieval-optimized network of confidence-weighted *generative* truths. Value lives in the edges and retrieval paths — not in the nodes themselves: a node's meaning is constituted entirely by its pattern of connections, and every edge spends from a finite per-node budget (the fan law). A KPM is the portable, distilled form of that network for a domain: it ships the irreducible generators of the domain's knowledge (not elaborations, not summaries), scored with earned evidential confidence, split into a sparse axiom index and a rich evidence store, and packaged with the operators needed to revise it. Because the generators transfer, the KPM transfers; because the confidence is evidence-gated, the KPM is auditable.

## The seven clusters

- [[A-structure]] — how knowledge is shaped: weighted edges, atomicity, foundherentist justification
- [[B-retrieval]] — how knowledge is recalled: spreading-activation = Hopfield = attention, cue-dependence, the capacity cliff, index/store split
- [[C-truth]] — confidence, correctness, and the limits of both: confidence earned not inferred, three independent orderings, confabulation risk, salience firewall
- [[D-dynamics]] — how knowledge changes over time: retrievability decay, novelty-gated write, MTT-safe consolidation, revision operators
- [[E-method]] — how to build and validate a KPM: layered distillation, retrieval practice, adversarial verification, lint/compile operators
- [[F-meta]] — what the doctrine knows about itself: convergence-corroboration, contradictions as category errors, the Surprise Principle, the B1 = B4 cognitive-map unification
- [[G-prospective]] — agentic and future-directed memory: trigger memory, intention lifecycle (agentic KPMs only)

## Operators (the productions)

A portable KPM ships axioms *and* the rules to revise them — the operators are its procedural memory.

- [[D4-contract]] — on contradiction, minimally shrink the belief set per AGM; never delete evidence
- [[D5-suppress]] — lower a belief's retrievability without touching its confidence or evidence; reversible, auditable
- [[E3-lint]] — mechanical pre-lock gate: atomicity, evidence presence, frontmatter-body sync, F2 invariant
- [[E5-compile]] — on impasse, distill the resolution path into a candidate new generator; must pass E4 before ignition

## How this package is built

The structure is self-exemplifying. The 23 atomic axiom notes *are* the index (B4's sparse index layer); the 41 evidence notes *are* the store (B4's rich content layer); this README is the distilled spine (E1's generator layer sitting above the elaboration). The lint gate runs automatically: `scripts/doctrine_lint.py` (0 violations). Every promoted axiom has been adversarially challenged and independently grounded (E4). Confidence fields are set from evidence, never from retrieval frequency or fluency (C1).

## How to use it

This doctrine is the rubric a knowledge-packaging skill or agent builds against when turning raw notes, research, or experience into a portable knowledge package:

1. **Distill generators, not notes** (E1) — find the irreducible source; don't transcribe elaborations.
2. **Score confidence from evidence** (C1) — check citations; never infer from fluency or recency.
3. **Split index from store** (B4) — KPM = index; research files = store; retrieval completes the join.
4. **Verify before locking** (E4) — run lint (E3) then adversarial challenge; Gettier risk is real.
5. **Mint, don't overwrite, on surprise** (the Surprise Principle, [[F3-surprise-principle]]) — large prediction error → new node, not in-place edit.
