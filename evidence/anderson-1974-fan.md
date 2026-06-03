---
id: anderson-1974-fan
type: evidence
ref: "Anderson, J. R. (1974). Retrieval of propositional information from long-term memory. Cognitive Psychology, 6(4), 451-474."
url: https://doi.org/10.1016/0010-0285(74)90021-8
verified: 2026-06-03
supports: [A1-fan-budgeted-edges]
proves: "Retrieval time rises monotonically with the number of facts associated to a concept (the fan effect); each additional link dilutes the activation budget available to the others."
limits: "Demonstrates the fan cost under experimental conditions with learned propositions; the ACT-R logarithmic formulation Sij = S − ln(fan) is the ACT-R 2.0 parameterization, not the 1974 paper directly."
---

# Anderson 1974 — The Fan Effect

Anderson's 1974 study established the foundational fan-effect result: participants
who learned more facts about a given person or location were reliably slower to
retrieve any single fact about that entity. Reaction time rose monotonically with
fan (number of associated propositions). The mechanism: each fact-association
competes for a finite per-node activation budget, so each additional link dilutes
the share received by all others.

The logarithmic formulation `Sij = S − ln(fanj)` — where S is a maximum
associative strength and fanj is the number of chunks associated to node j —
appears in the ACT-R 2.0 architecture (Anderson 1993), but the empirical law is
established here. This is the quantitative basis for [[A1-fan-budgeted-edges]]:
edges compete for a finite budget; adding a low-signal edge provably hurts the
retrieval of all others.
