---
id: amit-1985-capacity-cliff
type: evidence
ref: "Amit, D. J., Gutfreund, H., & Sompolinsky, H. (1985). Spin-glass models of neural networks. Physical Review Letters, 55(14), 1530–1533. Full replica derivation: Amit, Gutfreund & Sompolinsky (1987). Statistical mechanics of neural networks near saturation. Annals of Physics, 173, 30–67."
url: https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.55.1530
verified: 2026-06-03
supports: [B3-capacity-cliff]
proves: "Classical Hopfield networks undergo a sharp phase transition at α ≈ 0.138 (patterns/neurons): below this loading ratio retrieval is reliable; above it, retrieval collapses catastrophically to spurious attractors. The transition is a cliff, not a slope."
limits: "Derived for the classical binary Hopfield model under Hebbian learning. Modern continuous-Hopfield / attention models (Ramsauer 2020) escape the 0.138N ceiling via softmax, achieving exponential capacity — but retain an all-or-none ignition dynamic at the softmax temperature."
---

# Amit, Gutfreund & Sompolinsky 1985/1987 — Capacity cliff in Hopfield networks

Statistical-mechanics analysis (replica method) of classical Hopfield associative
memory under random pattern storage. Establishes the critical loading ratio α_c ≈
0.138: below it the network has a free-energy minimum at each stored pattern and
retrieval is robust; above it the free-energy landscape fills with spurious attractors
and the network no longer reliably retrieves any stored pattern. The 1987 Annals of
Physics paper gives the full replica derivation, confirming the phase transition and
its sharpness. This is the quantitative origin of the "capacity cliff" in the spine
and of the engineering mandate to shard rather than cram.

Used by [[B3-capacity-cliff]].
