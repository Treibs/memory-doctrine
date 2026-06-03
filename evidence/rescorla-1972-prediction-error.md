---
id: rescorla-1972-prediction-error
type: evidence
ref: "Rescorla, R. A. & Wagner, A. R. (1972). A theory of Pavlovian conditioning: Variations in the effectiveness of reinforcement and nonreinforcement. In A. H. Black & W. F. Prokasy (Eds.), Classical Conditioning II, pp. 64–99. Appleton-Century-Crofts."
url: http://www.scholarpedia.org/article/Rescorla-Wagner_model
verified: 2026-06-03
supports: [F3-surprise-principle]
proves: "Associative learning is driven by prediction error (λ − ΣV), not contiguity. Kamin blocking: pre-train A→US so V_A→λ; then compound AB→US. Because ΣV≈λ, prediction error ≈ 0, so ΔV_B ≈ 0 — B is not learned despite perfect pairing. The equation ΔV_A = α_A·β·(λ − ΣV) is mathematically the delta rule / LMS (Widrow–Hoff 1960), grounding modern gradient learning."
limits: "R–W minimizes total error and fails on some paradigms (latent inhibition, certain recovery effects) handled by attention-modulated successors (Mackintosh 1975; Pearce–Hall 1980, where α itself tracks uncertainty). Fixed-α is a simplification. The biological learning rate α is underspecified."
---

# Rescorla & Wagner 1972 — A Theory of Pavlovian Conditioning

The Rescorla–Wagner model formalized prediction error as the currency of associative
learning: `ΔV_A = α_A · β · (λ − ΣV)`, where `(λ − ΣV)` is the error between the
maximum supportable association (λ) and the already-predicted sum (ΣV). Learning stops
when prediction is perfect (error = 0), regardless of cue–outcome contiguity. Kamin's
blocking experiment is the proof: a pre-trained cue exhausts the error budget, leaving
nothing for a new co-trained cue. The equation is mathematically identical to the delta
rule (Widrow–Hoff 1960), linking associative learning to gradient descent.

Used by [[F3-surprise-principle]] as the behavioral level of description for the
Surprise Principle: the doctrine's three-zone write policy (no-PE → reinforce
retrievability; moderate-PE → reconsolidate; large-PE → mint new) is a direct
operational translation of the R–W error budget logic.
