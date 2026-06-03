---
id: C4-salience-gating
type: axiom
cluster: C-truth
title: Salience gates encoding strength but must not touch confidence
statement: >
  Arousal, emotional significance, and distinctiveness gate memory consolidation
  strength via amygdala-noradrenergic modulation (McGaugh 2004) and the von
  Restorff isolation effect. Salience is a legitimate WRITE-TIME gate that
  determines what earns a doctrine slot (promotion). But salience also inflates
  confidence and vividness WITHOUT improving accuracy (Talarico & Rubin 2003):
  flashbulb memories are subjectively more vivid and confidently-held yet
  factually no more consistent than ordinary memories. Therefore: salience is
  a promotion score (orthogonal to confidence), and the two scores must be stored
  separately. Collapsing them is the single most dangerous category error in a
  confidence-weighted store. Salience also links to prediction error (F3-
  surprise-principle): the same signed prediction-error signal that drives
  dopaminergic RPE is the mechanism by which salient / surprising events are
  encoded more strongly.
domain: salience-errors
generativity: 4
confidence: 0.91
status: locked
relations:
  derives-from: [C1-confidence-earned, C2-three-orderings]
  supports: [D2-novelty-gated-write, F3-surprise-principle]
  generalizes: []
  contradicts: []
  applies-to-kpm: [promotion-score, salience-confidence-orthogonality]
evidence: [mcgaugh-2004-amygdala, talarico-2003-flashbulb]
provenance: memory-research/salience-errors-deep
verification: {challenged: true, citations_checked: true, gate: "rt1+purge"}
---

# C4 · Salience gates encoding strength — but must not touch confidence

**The biological mechanism.** Post-training stress hormones (epinephrine,
corticosterone) activate the basolateral amygdala's noradrenergic system, which
modulates hippocampal consolidation in proportion to the significance of the
event (McGaugh 2004). The effect is *causal* (intra-amygdala propranolol blocks
peripherally administered epinephrine's enhancement), dose- and time-dependent,
and cue-independent. Memory is not a uniform recorder; it spends its consolidation
budget on the significant. This is the biological prior for a **promotion tier** in
a KPM: axioms flagged "significant" (by citation impact, cross-domain recurrence,
or operator judgment) get consolidated into the durable doctrine index tier.
McGaugh's own caveat is critical: emotional/salient memories are NOT more accurate
in detail — arousal buys *gist and central-detail enhancement* at the cost of
peripheral detail.

**The flashbulb dissociation.** Talarico & Rubin (2003) measured factual
consistency of 9/11 memories vs ordinary memories at 1, 6, and 32 weeks.
Consistency declined at the *same rate* for both. But confidence, vividness, and
"belief in accuracy" declined for everyday memories and *stayed high* for flashbulb
memories — a clean within-subjects confidence–accuracy dissociation. The salient
memory feels more accurate and retains that feeling even as it becomes equally
inconsistent.

**The doctrine consequence.** Salience does exactly two legitimate things:
1. It signals *what deserves a doctrine slot* (promotion gate — a write-time
   operation).
2. It predicts *subjective vividness and felt-confidence* — which are unreliable
   truth proxies and must therefore be **walled off from the `confidence` field**.

A KPM must therefore maintain two separate, orthogonal scores:

| Score | Set by | Changes when | Must not be set by |
|---|---|---|---|
| `salience` / promotion score | Significance, impact, cross-domain recurrence | Operator judgment at write time | Evidential review |
| `confidence` | Verified external evidence (C1) | New evidence arrives | Salience, retrieval frequency, vividness |

`kpm doctor` FAILS if any process raises `confidence` based on a node's salience
score, retrieval frequency, or vividness/fluency.

**Link to prediction error.** The same arousal signal that gates amygdala-mediated
consolidation is the behavioral signature of a **signed prediction error**: the
event was surprising, violated expectations, demanded an update. This connects C4
directly to [[F3-surprise-principle]] and [[D2-novelty-gated-write]] — the RPE /
reconsolidation mechanism is the agentic analogue of salience-gated encoding. The
three-zone write policy in F3 (no-PE → reinforce retrievability only; moderate-PE
→ reconsolidate; large-PE → new node) is the engineered form of the amygdala's
graded consolidation investment.

This axiom derives from [[C1-confidence-earned]] and [[C2-three-orderings]] (the
score-separation requirement), and supports [[D2-novelty-gated-write]] and
[[F3-surprise-principle]].

Evidence: [[mcgaugh-2004-amygdala]], [[talarico-2003-flashbulb]].
