---
id: E5-compile
type: operator
title: Compile-on-impasse (SOAR chunking)
trigger: "a query hits an impasse — no-cover, conflict, or multi-hop"
action: "the resolution path becomes a candidate new distilled generator; meta-axioms are chunks of repeated cross-domain impasses"
guardrail: "must pass E4 adversarial verification before it ignites (else SOAR's over-general-chunk bug; E4 guards correctness, not match-cost)"
governs: [E1-layered-distillation, E4-adversarial-verify]
---

# E5 · Compile-on-impasse

The write-side learning operator. Turns a resolved impasse into a new generator,
gated by [[E4-adversarial-verify]] and feeding [[E1-layered-distillation]].
