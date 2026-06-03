---
id: D4-contract
type: operator
title: Contract (AGM belief revision)
trigger: "a new finding contradicts a status:locked axiom"
action: "minimally shrink the belief set / lower entrenchment; never delete evidence"
guardrail: "reversible; logged; cannot push a confident axiom below its evidence floor"
governs: [C1-confidence-earned, F2-contradictions-category-errors]
---

# D4 · Contract

The revision operator. On contradiction, shrink minimally per AGM; preserve the
evidence store. Governs [[C1-confidence-earned]] and [[F2-contradictions-category-errors]].
