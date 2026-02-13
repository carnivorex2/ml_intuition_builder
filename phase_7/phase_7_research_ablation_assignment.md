# Phase 7 Assignment — Research Thinking: Hypothesis, Ablation, Insight

## Core Objective

This phase installs the final upgrade:

> Research is not building something new.  
> Research is isolating a variable and learning something true.

You will:
- Formulate a precise hypothesis.
- Design controlled experiments.
- Run ablations properly.
- Draw defensible conclusions.

No vague exploration.
No metric fishing.
No accidental insights.

Everything must be intentional.

---

# Deliverables

Your repository must contain:

- `research_question.md`
- `experiment_plan.md`
- `train.py`
- `results.md`
- `analysis.md`
- `limitations.md`

Reproducibility is mandatory.

---

# Step 1 — Define a Precise Research Question

Your research question must:

- Involve a concrete modeling decision.
- Be falsifiable.
- Be measurable.

Examples (you must create your own):

- Does increasing context length improve robustness under temporal shift?
- Does gated multimodal fusion improve stability under modality corruption?
- Does label smoothing improve calibration under distribution shift?
- Does smaller embedding dimension increase data efficiency?

Your question must include:

- What is being varied?
- What remains fixed?
- What metric determines success?

No vague questions like:
"Does this model work better?"

---

# Step 2 — Controlled Experiment Design

In `experiment_plan.md`, define:

## 1. Independent Variable
The one thing you are changing.

## 2. Controlled Variables
Everything that must remain constant:
- Dataset
- Split
- Training steps
- Optimizer
- Random seed(s)

## 3. Evaluation Protocol
- Primary metric
- Secondary metrics
- Statistical stability (multiple seeds if feasible)

## 4. Expected Outcome
State your prediction clearly.

You are allowed to be wrong.
You are not allowed to be vague.

---

# Step 3 — Implementation Discipline

Rules:

- Same data splits across experiments.
- Same preprocessing.
- Same training budget.
- Same evaluation protocol.

Log:
- Training curves
- Validation curves
- Parameter counts
- Runtime

If something differs unintentionally,
document it.

---

# Step 4 — Ablation Matrix

Design at least 3 controlled comparisons.

Example:

Variable: Context length

- 32 tokens
- 64 tokens
- 128 tokens
- 256 tokens

Measure:
- Accuracy
- Calibration
- Robustness under shift
- Training stability

Do not change multiple variables at once.

---

# Step 5 — Stress Under Shift

Evaluate your experimental variants under:

- Temporal shift
- Distribution shift
- Input corruption

Does your hypothesis still hold?

Research conclusions that only work IID are weak.

---

# Required Analysis

In `analysis.md`, answer:

1. Was your hypothesis correct?
2. How strong was the effect size?
3. Was improvement statistically stable?
4. Did tradeoffs emerge?
5. Did robustness differ from IID performance?
6. What surprised you?

Be quantitative.

---

# Step 6 — Limitations & Future Work

In `limitations.md`, address:

- What confounds might exist?
- What assumptions were fragile?
- What additional experiments would strengthen conclusions?
- What would invalidate your findings?

Be honest.

---

# Completion Criteria

You are done when:

- You can isolate a modeling variable cleanly.
- You can design controlled ablations.
- You can quantify effect size.
- You can explain why something works — not just that it works.
- You can admit uncertainty precisely.

---

# Why This Phase Matters

Engineering builds systems.

Research builds understanding.

Most practitioners never learn the difference.

If you complete this phase properly:

- You stop copying architectures blindly.
- You stop chasing trends.
- You start asking better questions.

That is the final upgrade.

You are no longer just building models.

You are learning how to learn.
