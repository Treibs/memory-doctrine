---
id: sarthi-2024-raptor
type: evidence
ref: "Sarthi, Abdullah, Tuli, Khanna, Goldie & Manning 2024, 'RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval', ICLR 2024, arXiv:2401.18059"
url: https://arxiv.org/abs/2401.18059
verified: 2026-06-03
supports: [E1-layered-distillation]
proves: "multi-level recursive summarization (a layered distillation tree) outperforms flat chunking on retrieval"
limits: "an empirical IR result, not a proof of the Shannon bound"
---

# Sarthi et al. 2024 — RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval

RAPTOR builds a **recursive tree** of abstractive summaries over a document corpus:
leaf nodes = raw chunks; higher nodes = LLM-generated cluster summaries at
progressively coarser granularity. At retrieval time, the system queries at any
level of the tree (or all levels), surfacing whichever granularity best answers the
query.

Key results: RAPTOR substantially outperforms flat-chunk RAG on question-answering
benchmarks requiring global or cross-section reasoning, where no single chunk contains
the answer. The tree-structure captures information that no single-level retrieval
can find.

This provides empirical support for [[E1-layered-distillation]]: the generator/summary
layer at the top is *necessary* for global retrieval; the detail layers are *necessary*
for local verification. Removing either level degrades performance — validating the
doctrine's prescription to distill the generator *and* keep the elaboration reachable
below.
