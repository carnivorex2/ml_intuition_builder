# Phase 2 Assignment — Time Series: Respecting the Arrow of Time

## Core Objective

This phase installs a non-negotiable instinct:

> The future must never inform the past.

You will:
- Build forecasting models.
- Accidentally cheat.
- Watch performance collapse when evaluated properly.
- Learn how temporal validation differs from random splitting.

This phase is about evaluation discipline under temporal structure.

---

# Deliverables

Your repository must contain:

- `train.py`
- `models/`
- `experiments.md`
- `postmortem.md`
- Clear documentation of:
  - Data preprocessing
  - Split strategy
  - Forecasting horizon
  - Baselines

No high-level trainer abstractions.

---

# Dataset Requirements

Choose a real-world time series forecasting dataset.

Constraints:
- At least 10,000 time steps total (can be multivariate)
- Clear temporal ordering
- Numeric features
- Forecasting task (predict future value(s))

Examples:
- Energy consumption
- Stock prices (use carefully — discuss volatility)
- Traffic volume
- Weather data
- Sales forecasting

Document:
- What is being predicted
- Forecasting horizon (e.g., next step, next 24 steps)
- Feature construction

---

# Part 1 — Naïve Baselines (Mandatory)

Before building neural models, implement:

1. Last value prediction
2. Moving average
3. Simple linear regression over lag features

Record:
- Training error
- Validation error
- Error across time

You are not allowed to skip this step.

Document:
- How strong are naïve methods?
- When do they fail?

---

# Part 2 — Incorrect Split (You Must Do This)

Randomly split the dataset into train and validation.

Train one of your models.

Record:
- Validation performance
- Why it looks good

Now answer:
- Why is this evaluation invalid?
- What information leaked?

This is intentional. You are required to do this incorrectly first.

---

# Part 3 — Proper Temporal Split

Implement a proper chronological split:

- Train on past
- Validate on strictly future data

Retrain all baselines.

Compare:
- Random split performance vs temporal split performance

Document:
- Magnitude of difference
- Why the performance changed
- Which models were most affected

---

# Part 4 — Neural Models

Implement at least two of the following:

- Feedforward network using lagged inputs
- Temporal CNN
- RNN (LSTM/GRU)
- Simple attention over time

You must:

- Define a clear forecasting window
- Clearly define input → target mapping
- Avoid leakage in feature construction

Experiment with:
- Sequence length
- Learning rate
- Model depth

Observe:
- Stability
- Overfitting
- Sensitivity to window size

---

# Part 5 — Rolling Evaluation

Implement rolling (walk-forward) validation:

- Train on [0:t]
- Validate on [t+1:t+k]
- Move window forward

Measure:
- Performance stability over time
- Degradation patterns

Document:
- Does performance drift?
- Are certain periods harder to predict?

---

# Required Analysis

In `postmortem.md`, answer:

1. How much did random splitting inflate performance?
2. Which model generalized best over time?
3. Did the neural network outperform naïve baselines?
4. How sensitive was performance to forecasting horizon?
5. What does overfitting look like in time series?
6. If deployed, how would this model fail?

Be specific and quantitative.

---

# Completion Criteria

You are done when:

- You can explain exactly why random splits are invalid for forecasting.
- You can detect temporal leakage immediately.
- You understand the strength of naïve baselines.
- You can implement rolling validation confidently.

---

# Why This Phase Matters

Time series forces you to confront:

- Leakage
- Distribution shift
- Non-stationarity
- Horizon-dependent difficulty

Later, video and audio will contain temporal structure.
If you do not master temporal evaluation now,
you will unknowingly cheat later.

Respect the arrow of time.