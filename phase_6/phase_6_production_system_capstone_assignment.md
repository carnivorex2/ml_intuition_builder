# Phase 6 Assignment — Capstone: Production-Grade ML System

## Core Objective

This phase installs the final instinct:

> A model is not the product. The system is the product.

You will design, implement, and evaluate an end-to-end ML system
under realistic production constraints.

This is not a Kaggle project.

This is a deployment simulation.

---

# Deliverables

Your repository must contain:

- `system_design.md`
- `train.py`
- `inference.py`
- `evaluate.py`
- `monitoring.md`
- `postmortem.md`

And:

- Reproducible training
- Reproducible evaluation
- Clear experiment tracking
- Runtime benchmarks

No hidden steps.

---

# Project Requirements

Choose a problem that includes at least TWO of the following:

- Temporal component
- Distribution shift risk
- Multimodal inputs
- Large-scale tabular features
- Streaming or near-real-time inference

You may reuse previous datasets but must extend them.

---

# Part 1 — System Design Document

Before writing code, create `system_design.md`.

It must include:

## 1. Problem Definition
- What is being predicted?
- What is the business objective?
- What metric truly matters?

## 2. Data Pipeline
- Data ingestion
- Feature construction
- Leakage prevention
- Versioning strategy

## 3. Model Architecture
- Why this model?
- Why not something simpler?
- Expected failure modes

## 4. Evaluation Strategy
- IID validation
- Temporal validation (if applicable)
- Shift evaluation
- Stress testing

## 5. Deployment Constraints
- Latency target
- Memory limit
- Throughput expectations

You may not begin coding until this is complete.

---

# Part 2 — Baseline Production Model

Implement the simplest viable system:

- Clean pipeline
- Simple model
- Clear evaluation

Benchmark:
- Accuracy
- Training time
- Inference latency
- Memory usage

This is your production baseline.

---

# Part 3 — Iterative Improvement

Improve the system under constraint:

You must improve at least ONE of:

- Accuracy
- Robustness under shift
- Latency
- Parameter efficiency

Without severely degrading the others.

Document:
- Tradeoffs
- What broke
- What improved

---

# Part 4 — Monitoring & Drift Simulation

Simulate post-deployment behavior:

- Introduce data drift
- Change class balance
- Introduce corrupted inputs

Measure:
- Performance degradation
- Confidence calibration shift
- Alert thresholds

Create `monitoring.md` containing:

- Drift detection strategy
- Metrics to monitor
- Retraining triggers
- Failure escalation plan

---

# Part 5 — Failure Injection

Intentionally break the system:

Examples:
- Drop a feature
- Delay inputs
- Truncate sequences
- Remove one modality

Measure:
- Catastrophic vs graceful degradation
- Recovery strategy

Document:
- What assumptions were brittle?
- What would crash production?

---

# Required Analysis

In `postmortem.md`, answer:

1. What was the biggest engineering bottleneck?
2. Did your evaluation predict real performance?
3. Where did complexity add value?
4. Where did complexity add risk?
5. If this were deployed tomorrow, what would fail first?
6. What would you redesign with 3 more months?

Be precise.

---

# Completion Criteria

You are done when:

- You can design an ML system before coding.
- You think in terms of constraints, not just models.
- You evaluate robustness automatically.
- You understand the difference between research metrics and production metrics.
- You can explain tradeoffs clearly.

---

# Why This Phase Matters

In the real world:

- Models drift.
- Pipelines break.
- Latency matters.
- Monitoring is mandatory.
- Simplicity wins more often than novelty.

The goal is no longer to win a leaderboard.

The goal is to ship something that survives contact with reality.

If you complete this phase properly,
you are no longer just training models.

You are building systems.
