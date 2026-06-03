---
id: anderson-1993-actr
type: evidence
ref: "Anderson, J. R. (1993). Rules of the Mind. Lawrence Erlbaum Associates."
url: https://doi.org/10.4324/9781315799438
verified: 2026-06-03
supports: [A1-fan-budgeted-edges]
proves: "ACT-R formalizes the spreading-activation fan law as Sij = S − ln(fanj), making the logarithmic dilution of associative strength a quantitative, measurable parameter of the architecture."
limits: "The logarithmic form is a fit to behavioral RT data; the precise constant S is fit per domain. The law is empirically grounded, not analytically derived from first principles."
---

# Anderson 1993 — ACT-R and the Logarithmic Fan Law

Anderson's *Rules of the Mind* (1993) presents the ACT-R 2.0 architecture and
formally states the spreading-activation associative strength equation:

`Sij = S − ln(fanj)`

where `Sij` is the strength of association from context element j to chunk i,
`fanj` is the number of chunks associated to element j (the fan), and S is the
maximum associative strength. The logarithm means that doubling fan costs less
than twice the activation — but every additional fan member provably costs
something. This is a logarithmic dilution law, not a linear 1/n split.

Used by [[A1-fan-budgeted-edges]] to ground the exact mathematical form of the
fan budget claim. The practical engineering implication: high-fan nodes must
curate their associations, because each addition carries a measurable retrieval
cost on every existing edge.
