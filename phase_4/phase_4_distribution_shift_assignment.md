# Phase 4 Assignment — Distribution Shift & Robustness

## Core Objective

This phase installs a critical production instinct:

> Your validation set is lying to you.

You will:
- Train models under one distribution.
- Evaluate under a shifted distribution.
- Watch performance degrade.
- Learn how to detect and reason about failure.

This phase is about robustness, not accuracy.

---

# Deliverables

Your repository must contain:

- `train.py`
- `evaluate.py`
- `experiments.md`
- `postmortem.md`
- Clear documentation of:
  - Training distribution
  - Evaluation distribution(s)
  - Shift type
  - Failure analysis

No high-level trainer abstractions.

---

# Dataset Requirements

Choose ONE of the following domains:

- Tabular classification
- Time series forecasting
- Text classification

Constraints:
- At least 10,000 samples
- Clearly separable subgroups or time segments
- Ability to simulate or identify distribution shift

You must define:

- Source distribution (train)
- Target distribution (test)

Examples of shifts:
- Time-based shift (train on early period, test on later)
- Subgroup shift (train on certain categories, test on others)
- Feature corruption
- Label imbalance change
- Vocabulary drift (for NLP)

You must clearly define the shift mechanism.

---

# Part 1 — Standard Training

Train your best-performing model from earlier phases.

Evaluate on:
- IID validation split (standard random split)

Record:
- Accuracy / loss
- Calibration (if classification)
- Error distribution

This is your "comfortable" baseline.

---

# Part 2 — Apply Distribution Shift

Now evaluate the same trained model on a shifted distribution.

Examples:
- Later time period
- Different subpopulation
- Corrupted inputs
- Class prior change

Do NOT retrain yet.

Measure:
- Performance drop
- Confidence shift
- Error type changes

Quantify degradation.

---

# Part 3 — Diagnose the Failure

Analyze:

- Which classes fail most?
- Which features changed most?
- Is the model overconfident under shift?
- Does performance degrade smoothly or catastrophically?

Visualize:
- Feature distribution comparison
- Prediction confidence histograms
- Error by subgroup

Document clearly.

---

# Part 4 — Mitigation Strategies

Implement at least one mitigation approach:

- Reweighting
- Domain-specific normalization
- Data augmentation
- Regularization adjustments
- Smaller model
- Temporal retraining (if time-based shift)

Retrain and re-evaluate.

Compare:
- Baseline vs mitigated performance
- Robustness improvement vs accuracy tradeoff

---

# Part 5 — Stress Testing

Intentionally degrade the input:

For example:
- Add noise
- Drop features
- Truncate text
- Perturb time windows

Measure:
- Sensitivity curve
- Performance vs corruption level

Document:
- Graceful degradation vs brittle failure

---

# Required Analysis

In `postmortem.md`, answer:

1. How large was the performance drop under shift?
2. Did validation performance predict real-world performance?
3. Was the model overconfident under shift?
4. Which mitigation strategy worked best?
5. What signals could have warned you earlier?
6. How would you monitor this model in production?

Be quantitative.

---

# Completion Criteria

You are done when:

- You no longer trust IID validation blindly.
- You understand distribution shift types.
- You can design robustness experiments deliberately.
- You can explain why models fail outside training distribution.

---

# Why This Phase Matters

In practice:

- Data drifts.
- Users change behavior.
- Sensors degrade.
- Language evolves.

Most ML failures are not optimization failures.

They are distribution failures.

If you can diagnose and mitigate shift,
you are operating at production-level thinking.
