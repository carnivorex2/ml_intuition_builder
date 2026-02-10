# Practical Model-Building Curriculum

**Goal**  
Develop real intuition for training machine learning models by repeatedly owning the full pipeline:
data → model → training → failure → iteration → reflection.

This curriculum prioritizes:
- end-to-end responsibility
- intentional failure
- lightweight, deployable models
- intuition over theory
- repetition across domains

PyTorch is the primary framework.

---

## Global Rules

- Every major project gets its own repo.
- Every repo contains:
  - `experiments.md` — running notes, surprises, failed ideas
  - `postmortem.md` — final reflection and lessons learned
- No pretrained models unless explicitly stated.
- You must be able to intentionally overfit a tiny dataset.
- If training behavior surprises you, stop and explain it.

---

## Phase 0 — Infrastructure & Control

**Purpose:** Remove tooling friction so failures are meaningful.

- Build a minimal PyTorch training spine:
  - explicit training loop
  - explicit validation loop
  - metric logging
  - checkpointing
- Define a standard repo structure and reuse it everywhere.
- Create a tiny synthetic dataset and overfit it on purpose.

**Intuition built:**  
> “I am in control of optimization and data flow.”

---

## Phase 1 — Tabular Data: Distrusting Metrics

**Purpose:** Learn how models lie.

- Train linear and tree-based baselines.
- Introduce a neural network and observe:
  - overfitting
  - instability
  - failure to beat trees
- Deliberately cause data leakage.
- Fix it and document the difference.

**Intuition built:**  
> “A good validation score can be meaningless.”

---

## Phase 2 — Time Series: Respecting Time

**Purpose:** Learn temporal honesty.

- Work on a forecasting task.
- Compare:
  - naïve baselines
  - feedforward models
  - temporal CNNs / recurrence
- Use incorrect random splits first.
- Replace with correct temporal splits.

**Intuition built:**  
> “The future leaks unless I actively prevent it.”

---

## Phase 3 — NLP: Representation vs Sequence

**Purpose:** Learn that structure often beats complexity.

- Text classification task.
- Compare:
  - bag-of-words
  - embeddings + pooling
  - attention-based models
- Observe data efficiency and failure modes.

**Intuition built:**  
> “Simple representations can outperform fancy models.”

---

## Phase 4 — Generic Temporal Modeling (Abstract)

**Purpose:** Isolate memory and state.

- Sequence-to-label or sequence-to-sequence task.
- Attempt with:
  - feedforward models (expect failure)
  - recurrence
  - attention over time
- Identify where information is lost.

**Intuition built:**  
> “Memory is fragile and expensive.”

---

## Phase 5 — Audio: Signals Over Time

**Purpose:** Combine time with continuous signals.

- Audio classification task.
- Compare modeling on:
  - raw waveform
  - spectrograms
- Keep architectures comparable.
- Observe optimization and data efficiency differences.

**Intuition built:**  
> “Representation is part of the model.”

---

## Phase 6 — Images: Spatial Inductive Bias

**Purpose:** Learn how models learn to see.

- Image classification from scratch.
- Build:
  - a naïve CNN
  - a deeper CNN
- Intentionally break training (normalization, depth, kernels).
- Recover.

**Intuition built:**  
> “Locality and hierarchy must be earned.”

---

## Phase 7 — Video: Compounding Difficulty

**Purpose:** Combine spatial and temporal reasoning.

- Video classification task.
- Start with frame-independent modeling (expect failure).
- Introduce temporal aggregation or 3D operations.
- Observe data hunger and instability.

**Intuition built:**  
> “Complexity compounds non-linearly.”

---

## Phase 8 — Lightweight Models (Cross-Domain)

**Purpose:** Develop architectural taste.

- Revisit models from multiple domains.
- Rebuild them with:
  - fewer parameters
  - simpler operations
- Compare performance vs size.
- Export at least one model (e.g., ONNX).

**Intuition built:**  
> “Constraints sharpen judgment.”

---

## Phase 9 — Modern Architectures (Contextualized)

**Purpose:** Understand why today’s models exist.

- Implement simplified versions of:
  - residual connections
  - attention
- Compare against earlier baselines.
- No pretrained weights.

**Intuition built:**  
> “Successful architectures solve specific pain points.”

---

## Phase 10 — Cold-Start Synthesis

**Purpose:** Prove independence.

- Pick a dataset you’ve never seen.
- No tutorials.
- No copying prior models.
- Build the best lightweight model you can.
- Write a full postmortem.

**Intuition built:**  
> “I can approach a new dataset with confidence.”

---

## End State

By the end of this curriculum you should have:
- multiple clean, focused repos
- a personal training framework you understand deeply
- instincts for:
  - convergence
  - overfitting
  - representation choice
  - architectural tradeoffs
- confidence owning the full modeling lifecycle

