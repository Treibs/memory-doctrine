---
id: E3-lint
type: operator
title: Lint (structural pre-lock checks)
trigger: "before a note is committed or a belief is locked"
action: "run structural checks — atomicity, >=1 evidence, frontmatter<->wikilink sync, the F2 no-contradiction invariant"
guardrail: "a lint failure blocks the lock; lints check structure, not truth"
governs: [A2-atomicity, E4-adversarial-verify, F2-contradictions-category-errors]
---

# E3 · Lint

The mechanical gate that runs before the judgment gate. Enforces
[[A2-atomicity]], feeds [[E4-adversarial-verify]], and asserts
[[F2-contradictions-category-errors]] as an invariant.
