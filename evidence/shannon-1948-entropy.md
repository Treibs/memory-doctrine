---
id: shannon-1948-entropy
type: evidence
ref: "Shannon, C.E. (1948). 'A Mathematical Theory of Communication.' Bell System Technical Journal 27:379–423, 623–656."
url: https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf
verified: 2026-06-03
supports: [E1-layered-distillation]
proves: "Theorem 9 (Noiseless Coding): the mean codeword length cannot drop below H = −Σ pᵢ log pᵢ; H is the irreducible lower bound on lossless compression. Redundancy above H is recoverable; the generator is the source's irreducible H."
limits: "A theorem about stationary ergodic sources; 'joint entropy of an axiom-set' over a typed-edge graph has no off-the-shelf estimator — the invariant is a principle, not yet an executable lint."
---

# Shannon 1948 — A Mathematical Theory of Communication

The founding paper of information theory. Theorem 9 establishes entropy H as the
absolute floor for lossless compression: no encoding can transmit above C/H
symbols/second, and no code can have a mean length below H bits/symbol.

**Theorem 9 (direct quote):** "Let a source have entropy H … and a channel … capacity C … it is possible to encode … to transmit at the average rate C/H … It is not possible to transmit at an average rate greater than C/H."

**Redundancy (§7):** "One minus the relative entropy is the redundancy … The redundancy of ordinary English … is roughly 50% … half of what we write is determined by the structure of the language and half is chosen freely."

This grounds [[E1-layered-distillation]]: the generator ≈ the freely-chosen H; the
elaboration ≈ the structural redundancy above H. Redundancy can be stripped losslessly;
the generator cannot be compressed further without loss.
