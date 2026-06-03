---
id: agm-1985-belief-revision
type: evidence
ref: "Alchourrón, C. E., Gärdenfors, P., & Makinson, D. (1985). On the Logic of Theory Change: Partial Meet Contraction and Revision Functions. Journal of Symbolic Logic, 50(2), 510-530."
url: https://doi.org/10.2307/2274239
verified: 2026-06-03
supports: [A3-foundherentist-generativity]
proves: "Epistemic entrenchment — the ordering that determines which beliefs a rational agent surrenders last — is the formal definition of what the KPM calls 'generativity'; the AGM rationality postulates make revision and contraction well-defined operators on a belief corpus."
limits: "AGM assumes a classical, consistent logical theory as the belief state; real KPM graphs are paraconsistent (can hold local contradictions) and weighted, so the postulates apply as design inspiration rather than directly executable constraints."
---

# AGM 1985 — On the Logic of Theory Change

Alchourrón, Gärdenfors & Makinson's 1985 paper is the canonical foundation of
formal belief revision. It establishes three typed operators — **expansion**
(add a belief, no consistency check), **contraction** (remove a belief while
disturbing as little else as possible), and **revision** (add a belief while
restoring consistency) — and the rationality postulates constraining them.

The load-bearing result for [[A3-foundherentist-generativity]] is **epistemic
entrenchment** (Gärdenfors & Makinson 1988 formalization): the total preorder `≤`
over beliefs where `p ≤ q` means "I would give up p before q." When forced to
contract, you surrender the *least-entrenched* belief first. Postulates include:
- **Dominance:** if `p ⊢ q` then `p ≤ q` (more specific/derived beliefs are less
  entrenched than their generators).
- **Maximality:** tautologies are maximally entrenched.

This formal structure *is* the KPM's `generativity` field made precise:
high-generativity axioms = high epistemic entrenchment = surrendered last. The
Dominance postulate also confirms the doctrine's claim that derived findings are
less entrenched than their generators — exactly why periphery is revised before
core.
