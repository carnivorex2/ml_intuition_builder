# Phase 8 Assignment — Constraint-Driven Design & Strategic Tradeoffs

## Core Objective

This phase installs the final systems instinct:

> The best model under no constraints is irrelevant.  
> The best model under real constraints wins.

You will:
- Design an ML system under severe constraints.
- Make explicit tradeoffs.
- Justify architectural decisions strategically.
- Choose what NOT to optimize.

This is not an implementation-heavy phase.

This is a decision-heavy phase.

---

# Deliverables

Your repository must contain:

- `problem_context.md`
- `constraints.md`
- `architecture_proposal.md`
- `tradeoff_analysis.md`
- `evaluation_plan.md`
- `failure_modes.md`

Implementation is optional but encouraged.

The thinking is mandatory.

---

# Step 1 — Define a Realistic Scenario

Create a deployment scenario with hard constraints.

Examples:

- On-device inference on mobile
- Real-time anomaly detection in streaming telemetry
- Low-bandwidth remote monitoring
- High-frequency financial signal prediction
- Safety-critical medical support system

Your scenario must define:

- Who uses the system
- What failure costs
- What latency is tolerable
- What compute is available
- What data arrives and how often

Make it concrete.

---

# Step 2 — Hard Constraints (Non-Negotiable)

Define at least five hard constraints, such as:

- < 50ms latency
- < 20MB memory
- No GPU at inference
- Model retraining only once per month
- Limited labeled data
- High distribution shift risk
- Privacy restrictions

These constraints must shape your architecture.

You are not allowed to ignore them later.

---

# Step 3 — Architecture Proposal

In `architecture_proposal.md`, describe:

## 1. Model Choice
- Why this class of model?
- Why not a larger one?
- Why not a more complex one?

## 2. Feature Pipeline
- What is precomputed?
- What is done at inference?
- Where can leakage occur?

## 3. Training Strategy
- Data refresh cadence
- Validation protocol
- Shift detection strategy

## 4. Fallback Strategy
- What happens if the model fails?
- Is there a heuristic backup?

---

# Step 4 — Explicit Tradeoff Table

In `tradeoff_analysis.md`, create a table:

| Dimension | Option A | Option B | Chosen | Why |
|-----------|----------|----------|--------|-----|
| Accuracy | High | Medium | Medium | Meets latency constraint |
| Latency | 120ms | 35ms | 35ms | Under SLA |
| Model Size | 80MB | 15MB | 15MB | Mobile limit |
| Robustness | Medium | High | Medium | Acceptable risk |

You must justify tradeoffs explicitly.

No vague reasoning.

---

# Step 5 — Evaluation Strategy Under Constraint

In `evaluation_plan.md`, define:

- Offline metrics
- Online metrics
- Monitoring metrics
- Alert thresholds
- Rollback criteria

Answer:

- What metric truly matters?
- When would you disable the model?
- What does safe degradation look like?

---

# Step 6 — Failure Modes

In `failure_modes.md`, analyze:

- Worst-case scenario
- Most likely failure
- Silent failure risks
- Overconfidence under shift
- Data pipeline failure
- Monitoring blind spots

Be concrete.

---

# Required Analysis

You must answer:

1. What performance did you intentionally sacrifice?
2. What constraint dominated the design?
3. What is the highest-risk assumption?
4. Where could hidden coupling cause collapse?
5. If you doubled compute, what would change?
6. If you halved compute, what would break?

---

# Completion Criteria

You are done when:

- You think in tradeoff space automatically.
- You optimize under constraints rather than in isolation.
- You can defend architectural decisions.
- You can justify not using a larger model.
- You can explain failure modes before they happen.

---

# Why This Phase Matters

Most ML engineers optimize models.

Senior engineers optimize systems.

Principals optimize tradeoffs.

The real skill is not maximizing metrics.

It is selecting the right compromise under constraint.

If you complete this phase properly,
you are no longer reacting to problems.

You are anticipating them.
