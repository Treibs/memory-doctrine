---
id: haack-1993-independent-security
type: evidence
ref: "Haack, S. (1993). Evidence and Inquiry: Towards Reconstruction in Epistemology. Blackwell, Oxford. (Specifically: the independent-security criterion and its role in preventing circular justification.)"
url: https://www.wiley.com/en-us/Evidence+and+Inquiry%3A+Towards+Reconstruction+in+Epistemology-p-9780631116325
verified: 2026-06-03
supports: [E4-adversarial-verify]
proves: "A belief is well-grounded only if its supporting evidence is *independently secure* — obtained and assessed without circularity relative to the belief it supports. Justification strength is a function of supportiveness × independent security × comprehensiveness. Convergence of independently acquired evidence across multiple lines is the strongest available corroboration."
limits: "Normative epistemology, not an empirical result. 'Independent security' must be operationalized for machine belief systems — in a KPM context this means the cited source must be primary and verifiable, not a self-referential chain of AI outputs."
---

# Haack 1993 — Independent Security (adversarial-verify facet)

A distinct claim from the foundherentism synthesis: the **independent security**
criterion. Within Haack's warrant calculus, justification = f(supportiveness,
**independent security**, comprehensiveness). Independent security is the anti-
circularity condition: evidence *e* is independently secure for belief *B* only if
*e* is obtained and assessed without relying on *B* or any belief in *B*'s support
chain.

This is the formal basis for [[E4-adversarial-verify]]:

- "Adversarial challenge" operationalizes independent security: the challenger must
  attempt falsification using *different* evidence than was used to establish the
  belief — closing the circular-justification loophole.
- "Citation check" verifies that the anchor source is a primary document, correctly
  quoted, and that the quoted passage actually supports the claim (not a chain of
  AI-mediated paraphrases).
- "Refute-by-default" implements the presumption that a belief is *not* independently
  secure until the adversarial pass has failed to find a defeater.
- "Convergence across independent challenges = corroboration" (relates [[F1-convergence-corroboration]]): when multiple independent adversarial lines
  all fail to defeat *B*, that convergent failure is Haack's strongest corroboration —
  the crossword analogy at scale.

Note: the broader foundherentist synthesis (crossword analogy, foundational structure)
is treated in the companion note `haack-1993-foundherentism`, which supports
`A3-foundherentist-generativity`. This note isolates the adversarial-security facet
used by E4.
