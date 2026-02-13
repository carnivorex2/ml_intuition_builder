# Phase 1 Assignment — Tabular Data: Learning to Distrust Metrics

## Core Objective

This phase exists to install one permanent instinct:

> A validation score is meaningless unless I deeply trust how it was produced.

You will:
- Build strong baselines.
- Build a neural network.
- Accidentally (and intentionally) fool yourself.
- Fix your evaluation.
- Explain what went wrong.

This is not about leaderboard chasing.
This is about epistemic discipline.

---

# Deliverables

Your repository must contain:

- `train.py`
- `models/`
- `experiments.md`
- `postmortem.md`
- Saved model checkpoints
- A README that explains:
  - Dataset chosen
  - Train/validation split strategy
  - Baseline performances
  - Final model performance

No high-level trainer frameworks allowed.

---

# Dataset Requirements

Choose a real-world tabular classification dataset.

Constraints:
- ≥ 5,000 rows
- ≥ 10 features
- Binary or multiclass classification
- No images, no audio, no raw text
- Features must be numeric or convertible to numeric

Examples (do not blindly pick — choose intentionally):
- Credit default prediction
- Medical diagnosis
- Fraud detection
- Marketing conversion prediction

Document:
- What each feature represents
- Which features seem predictive
- Any suspicious columns

---

# Part 1 — Linear Baseline

Implement logistic regression (or equivalent single-layer neural model).

You must train:

1. Without feature normalization
2. With feature normalization

Record:
- Training loss
- Validation loss
- Accuracy (or appropriate metric)

Analyze:
- Did normalization matter?
- Did regularization matter?
- What does overfitting look like here?

---

# Part 2 — Tree-Based Baseline

Use a tree-based model (e.g., Random Forest or Gradient Boosting).

Compare:
- Validation performance vs linear model
- Overfitting tendencies
- Sensitivity to feature scaling

Document:
- Why might trees outperform linear models?
- What patterns can trees capture that linear models cannot?

---

# Part 3 — Neural Network (Expect Instability)

Build a small MLP:

- At least 2 hidden layers
- Nonlinear activations
- Explicit training loop
- No automated trainer APIs

You must experiment with:
- Depth
- Width
- Learning rate
- Regularization

Observe:
- Does it overfit faster than trees?
- Does it beat trees?
- Is it sensitive to hyperparameters?

Document everything in `experiments.md`.

---

# Part 4 — Intentionally Break Validation

You must deliberately create at least two flawed evaluation setups.

Examples:

- Random split when data has time ordering
- Leakage by including a target-derived feature
- Normalizing using full dataset before splitting
- Duplicate rows across splits

Train a model under flawed evaluation.

Record:
- Validation performance
- Why it looks impressive
- Why it is wrong

Then fix the issue.

Compare before vs after.

This is the most important part of Phase 1.

---

# Required Analysis

In `postmortem.md`, answer:

1. Which model performed best and why?
2. Did the neural network justify its complexity?
3. What caused the largest artificial performance inflation?
4. How can you detect leakage early?
5. What signals indicate overfitting in tabular data?
6. If you had to deploy one model, which would it be and why?

Be precise. No vague generalities.

---

# Completion Criteria

You are done when:

- You can clearly explain why trees often dominate tabular tasks.
- You can intentionally create and then eliminate data leakage.
- You understand how normalization interacts with linear models.
- You no longer blindly trust a validation score.

---

# Why This Phase Matters

Vision and audio will feel harder.

But tabular data is where smart people learn the most dangerous lesson:

> The model is not the hardest part.
> Evaluation is.

Master this now.