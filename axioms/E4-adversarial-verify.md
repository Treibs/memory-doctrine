---
id: E4-adversarial-verify
type: axiom
cluster: E-method
title: Beliefs are locked only after adversarial challenge + citation check
statement: >
  A belief may not be promoted to the doctrine tier until it has survived an
  adversarial challenge (an independent agent attempts falsification using evidence
  other than what supported it) and a citation check (every anchor source is primary,
  correctly quoted, and actually supports the claim). Convergence across independent
  challenges is corroboration. Refute-by-default — the challenger presumes the belief
  is false until it cannot be falsified.
domain: ai-machine
generativity: 5
confidence: 0.93
status: locked
relations:
  derives-from: []
  supports: [F1-convergence-corroboration]
  generalizes: []
  contradicts: []
  applies-to-kpm: [promotion-gate, kpm-doctor-citcheck, lock-ritual]
evidence: [haack-1993-independent-security]
provenance: memory-research/ai-machine
verification: {challenged: true, citations_checked: true, gate: "rt1+rt3"}
---

# E4 · Adversarial verification is the anti-Gettier guardrail

A belief can be **true**, **believed**, and **justified** yet still fail to constitute
knowledge — Gettier (1963) showed that justified true belief is insufficient if the
justification is accidentally connected to the truth. The adversarial verification
protocol is the operational anti-Gettier guardrail: it closes the accidental-
justification loophole by requiring that the justification hold *even when an
independent agent actively tries to break it*.

**The three components:**

1. **Adversarial challenge.** A challenger — independent of the author — attempts to
   falsify the belief using *different* evidence than was used to support it. This
   operationalizes Haack's **independent security** criterion ([[haack-1993-independent-security]]): the supporting evidence must be obtained and assessed without
   circularity. The challenger must use independent cues; if they cannot locate a
   defeater, confidence rises. *Refute-by-default*: the presumption is that the belief
   is not independently secure until falsification has been attempted and failed.

2. **Citation check.** Every cited source is verified as: (a) a real, primary document
   (not a chain of AI paraphrases); (b) correctly quoted or summarized; (c) actually
   supporting the specific claim made, not a related but distinct claim in the same
   source. This closes the misattribution failure mode (Schacter's *Seven Sins*).

3. **Convergence = corroboration.** When multiple *independent* adversarial lines all
   fail to defeat the belief, their convergence is the strongest available corroboration
   (relates [[F1-convergence-corroboration]]). This is the crossword analogy at scale:
   many independent constraints all accepting the same entry raise confidence more than
   a single strong anchor. Where convergence is a *theorem* (e.g. Hopfield ↔ attention),
   it licenses certainty; where it is empirical convergence (e.g. cognition and AI
   arriving at the same architecture), it licenses strong support but not certainty.

**Relation to [[E3-lint]] and [[E5-compile]]:** E4 is the gate that must be passed
before any candidate axiom (including one produced by E5 self-compilation) can be
promoted. E3 lints structural properties (schema, fan, singleton); E4 verifies
epistemic properties (truth, citation). They are complementary, not redundant.

**Guarding E5:** when a self-compiled chunk (E5-compile) reaches the promotion
threshold, it must pass E4 before igniting — this prevents SOAR's over-general-chunk
failure mode (a plausible-sounding but insufficiently tested generalization hardening
into a doctrine node). E4 guards *correctness*; E5 guards *generativity*.

**The `kpm doctor` check:** every axiom in the locked tier carries a
`verification: {challenged: true, citations_checked: true}` field. `kpm doctor` fails
any axiom promoted to the doctrine tier without this field populated. The lock ritual
records which red-team(s) provided the challenge.
