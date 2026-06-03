---
id: shannon-1959-rate-distortion
type: evidence
ref: "Shannon, C.E. (1959). 'Coding Theorems for a Discrete Source With a Fidelity Criterion.' IRE National Convention Record 7:142–163."
url: https://gwern.net/doc/cs/algorithm/information/1959-shannon.pdf
verified: 2026-06-03
supports: [E1-layered-distillation, C3-confident-but-wrong]
proves: "The rate-distortion function R(D) is the minimum bits/letter to reproduce a source within distortion D. R(0) = H (zero distortion = full entropy). You cannot go below R(D) without exceeding distortion D. Every bit saved below H buys a quantified, mandatory amount of error."
limits: "Defines R(D) for stationary sources; computing R(D) for a discrete typed-graph axiom-set requires a distortion metric over beliefs — no standard implementation exists."
---

# Shannon 1959 — Rate-Distortion Theory

The companion theorem to the 1948 paper, extending it into the *lossy* regime.

**R(D) definition (direct quote):** "there exists a function R(d) … which measures … the equivalent rate R of the source (in bits per letter produced) when d is the allowed distortion level … For coding purposes where a level d of distortion can be tolerated, the source acts like one with information rate R(d)."

Key property: R(D) is **monotone-decreasing and convex**; R(0) = H; R(D) → 0 only
as D → ∞. Every point on the curve represents a **mandatory trade-off**: a saved bit
implies a quantified distortion.

This grounds [[E1-layered-distillation]] in two ways:

1. The *lossless* regime (elaboration-stripping) is safe because elaboration is
   recoverable redundancy above H — the source stays at R(0) = H.
2. Any *gist* or interpolated node that compresses below H lives at some D > 0 on
   the R(D) curve. That distortion is not a bug; it is the mathematical price of the
   compression, and it is the formal root of C3 (confident-but-wrong in any gist store).
