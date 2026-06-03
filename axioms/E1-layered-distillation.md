---
id: E1-layered-distillation
type: axiom
cluster: E-method
title: Distillation is Shannon-bounded layering, not lossy compression
statement: >
  Knowledge is distilled in layers (generators → elaboration → evidence store).
  Shannon bounds this exactly: the generator ≈ the source's irreducible entropy H;
  elaboration ≈ recoverable redundancy above H. Redundancy can be stripped
  losslessly; the generator cannot be compressed below H without lossy distortion
  priced by the rate-distortion curve R(D). This is the mathematical root of C3.
domain: information-theory
generativity: 5
confidence: 0.93
status: locked
relations:
  derives-from: []
  supports: [C3-confident-but-wrong, B4-index-store-split]
  generalizes: []
  contradicts: []
  applies-to-kpm: [distillation-policy, shard-method, kpm-doctor-invariant]
evidence: [shannon-1948-entropy, shannon-1959-rate-distortion, sarthi-2024-raptor]
provenance: memory-research/forgetting-infotheory-collective-deep
verification: {challenged: true, citations_checked: true, gate: "rt3+purge"}
---

# E1 · Layered distillation is Shannon-bounded

Distillation operates in layers. At the top sits the **generator** — the irreducible
conceptual claim from which elaboration can be recovered. Below it lies the
**elaboration** — the structured redundancy that makes the generator concrete,
memorable, and re-derivable. Below that, linked but not duplicated, sits the
**evidence store** — the primary sources at D=0 fidelity.

Shannon's Noiseless Coding Theorem ([[shannon-1948-entropy]]) supplies the formal
ceiling: the mean codeword length cannot fall below H = −Σ pᵢ log pᵢ. The generator
is the source's H — the *freely chosen* half, as Shannon put it (English has ~50%
redundancy; the other 50% is structurally determined and recoverable). Elaboration
is the recoverable redundancy above H: you may strip it **losslessly** because it is
derivable from the generator given shared context. You may **not** compress the
generator below H without entering the lossy regime.

That lossy regime is governed by Shannon's rate-distortion function ([[shannon-1959-rate-distortion]]): R(D) is the minimum bits/letter achievable at distortion D. R(0) = H;
every bit saved below H buys mandatory distortion. Any gist or summary node that
compresses below the axiom-set's joint entropy sits at some D > 0 on the R(D) curve —
and the distortion it carries is not a bug but the **mathematical price of the
compression**. This is the formal root of [[C3-confident-but-wrong]]: gist distortion
is priced, mandatory, and must never be hidden.

RAPTOR ([[sarthi-2024-raptor]]) provides empirical validation: a recursive multi-level
tree of summaries outperforms flat chunking on global retrieval tasks precisely
because the generator layer captures cross-document structure that no single chunk
holds, while the detail layers preserve local fidelity. Removing either layer
degrades retrieval — confirming the prescription: distill the generator *and* keep
the elaboration reachable.

**KPM invariant:** a node tagged "distilled" must be either (a) pure redundancy-
stripping with the elaboration recoverable from the generator + evidence (lossless,
D=0), or (b) a gist/interpolation at D>0 tagged as such, never inheriting a stored
node's confidence (enforcing [[C3-confident-but-wrong]]). The axiom-set's joint
entropy is the floor `kpm doctor` should enforce — a KPM may not claim lossless
compression below H.

**Relation to [[B4-index-store-split]]:** the generator/elaboration/evidence stack *is*
the index/store split realized at the intra-node level: the generator indexes into
elaboration, which indexes into evidence. The macro B4 split and the micro E1 layering
are the same architecture at different scales.

**Caveat (from the spine lock record):** E1 is a principle and invariant, not yet
an executable lint. No off-the-shelf estimator exists for the joint entropy H of a
typed-edge axiom-set. `kpm doctor` cannot yet measure it; the invariant is enforced
by architectural convention (separate generator/elaboration fields, distortion-tagged
gist nodes) until an estimator is implemented.
