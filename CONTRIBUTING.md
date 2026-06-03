# Contributing — challenge this doctrine

This doctrine is **defeasible by design.** Every axiom is confidence-weighted and was
adversarially reviewed before it locked — but "locked" means *current best*, not *final*.
The fastest way to improve it is to attack it. Challenges are the feature, not the nuisance.

## Try to break an axiom

Open an issue titled `challenge: <axiom-id>` (e.g. `challenge: C3-confident-but-wrong`) with:

1. **Which axiom** (its id, e.g. `B4-index-store-split`).
2. **The kind of challenge:**
   - **Refute** — you think the axiom is wrong. Show a counter-example or contradicting evidence.
   - **Confidence** — you think the `confidence` score is too high/low. Say why; cite.
   - **Scope** — it's true but over/under-stated, or its `domain` is wrong.
   - **Citation** — an `evidence/` note misattributes, mis-cites, or links a dead/wrong source.
3. **Your evidence** — a real, checkable citation (paper, DOI, dataset). Unsourced opinions
   move the confidence needle very little; a cited counter-example moves it a lot.

That's it. A well-cited refutation that survives discussion will lower an axiom's confidence,
re-scope it, or retire it — and you'll be credited.

## Propose a new axiom or evidence

Open a PR that adds a note following the existing schema (copy any file in `axioms/` or
`evidence/`). Requirements the lint enforces:

- `axioms/<id>.md` — `id` matches the filename; `confidence` in `[0,1]`; `generativity` in
  `1..5`; every `relations` target resolves and appears as a wikilink in the body; at least
  one `evidence` id; no `contradicts` edge to a `locked` axiom.
- `evidence/<id>.md` — a real source with a `url` and a `verified` date; `proves` and `limits`.
- Run `python3 scripts/doctrine_lint.py .` — it must report `0 violations`. Then `kpm doctor`.

## How beliefs change here

The doctrine carries its own revision operators (see `operators/`): `D4-contract` (shrink
minimally on contradiction, never delete evidence), `D5-suppress` (lower retrievability,
reversibly), `E3-lint` (the structural gate), `E5-compile` (distill a resolved impasse into a
new generator). Disagreements are resolved by these, not by argument-from-authority. Apparent
contradictions are usually category errors (F2): we split the conflated term and keep both halves.

## License

Content is **CC BY 4.0** (adapt and improve with attribution); the scripts are MIT. By
contributing you agree your contribution ships under the same terms.
