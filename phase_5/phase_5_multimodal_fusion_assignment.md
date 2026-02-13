# Phase 5 Assignment — Multimodal Learning: Fusion & Failure Modes

## Core Objective

This phase installs a system-level instinct:

> Adding modalities increases complexity faster than it increases signal.

You will:
- Combine two modalities.
- Compare unimodal vs multimodal performance.
- Analyze when fusion helps — and when it hurts.
- Investigate modality dominance and failure behavior.

This phase is about architectural reasoning.

---

# Deliverables

Your repository must contain:

- `train.py`
- `models/`
- `fusion.py`
- `experiments.md`
- `postmortem.md`
- Clear documentation of:
  - Each modality pipeline
  - Fusion strategy
  - Parameter counts
  - Training stability

No end-to-end pretrained multimodal models.

---

# Dataset Requirements

Choose a dataset with at least two modalities:

Examples:
- Text + tabular metadata
- Text + time series signals
- Image + tabular features
- Audio + metadata
- Video + structured signals

Constraints:
- At least 10,000 samples (or sufficiently large sequences)
- Supervised prediction task
- Modalities must provide non-redundant information

You must justify:
- What each modality contributes
- Why fusion might help

---

# Part 1 — Unimodal Baselines (Mandatory)

Train separate models for each modality:

Model A: Modality 1 only  
Model B: Modality 2 only  

Record:
- Validation performance
- Parameter count
- Training time
- Stability

Document:
- Which modality is stronger?
- Is one clearly dominant?

This step is required.

---

# Part 2 — Simple Fusion

Implement early or late fusion:

Early fusion:
- Concatenate learned representations
- Feed into joint classifier

Late fusion:
- Combine logits or probabilities

Train and compare against unimodal models.

Measure:
- Performance improvement (if any)
- Overfitting risk
- Convergence behavior

---

# Part 3 — Ablation Study

Perform structured ablations:

- Remove one modality after training
- Add noise to one modality
- Drop one modality at inference

Measure:
- Performance sensitivity
- Modality dependence

Document:
- Is the model robust to missing inputs?
- Does one modality dominate?

---

# Part 4 — Fusion Variants

Implement at least one alternative fusion strategy:

Options:
- Gated fusion
- Attention-based fusion
- Weighted averaging with learned weights
- Feature-level interaction (e.g., bilinear interaction)

Keep the architecture interpretable.

Compare:
- Parameter efficiency
- Stability
- Improvement over simple fusion

---

# Part 5 — Modality Imbalance Experiment

Intentionally weaken one modality:

Examples:
- Reduce training data for one modality
- Corrupt features
- Truncate sequences

Observe:
- Does the model adapt?
- Does it collapse?
- Does it over-rely on the stronger modality?

---

# Required Analysis

In `postmortem.md`, answer:

1. Did multimodal fusion meaningfully outperform unimodal models?
2. Which fusion strategy worked best?
3. Was the model robust to missing modalities?
4. Did training become less stable with fusion?
5. Did parameter count scale linearly or explosively?
6. When is multimodal modeling actually worth it?

Be quantitative and specific.

---

# Completion Criteria

You are done when:

- You can justify when to add a modality.
- You understand early vs late fusion tradeoffs.
- You can detect modality dominance.
- You can design ablation experiments deliberately.

---

# Why This Phase Matters

Real-world systems are multimodal:

- Autonomous systems (vision + lidar + telemetry)
- Assistants (text + audio + context)
- Medical systems (imaging + tabular + notes)

But:

- More inputs ≠ better performance.
- Fusion adds failure modes.
- Complexity increases brittleness.

You must learn to add signal — not noise.

If you cannot justify multimodal design choices,
you are guessing.

This phase ensures you are not guessing.
