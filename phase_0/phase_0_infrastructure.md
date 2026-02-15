# Phase 0 Assignment — Infrastructure & Control

## Objective

Before training real models, you must prove that:

> You control the training process.

This phase is not about performance.  
It is about ownership.

If something fails later in this curriculum, it should never be because
you don’t understand your training loop.

---

# Deliverables

Your repo must contain:

- `train.py`
- `models/`
- `data/`
- `experiments.md`
- `postmortem.md`
- At least one saved checkpoint

Your code must not rely on high-level training wrappers.
No Lightning. No trainer abstractions.
You write the loop.

---

# Part 1 — Build Your Training Spine

Implement a minimal but complete PyTorch training framework.

It must include:

### 1. Explicit Training Loop
- Forward pass
- Loss computation
- Backward pass
- Optimizer step
- Gradient zeroing

### 2. Explicit Validation Loop
- Model in eval mode
- No gradient tracking
- Separate metric computation

### 3. Logging
At minimum, log:
- Training loss
- Validation loss
- At least one metric (e.g., accuracy)

Print clean, readable logs.

---

# Part 2 — Synthetic Dataset (You Must Overfit)

Create a small synthetic dataset manually.

Requirements:
- Very small (e.g., 50–200 samples)
- Simple pattern (linearly separable or slightly nonlinear)
- Fully controlled by you

Examples:
- 2D points with a decision boundary
- Random vectors with a deterministic label rule

Train a small model on this dataset.

### Your model must:

- Reach near-zero training loss
- Reach near-100% training accuracy

If it does not:
- You are not in control.
- Fix it.

Document:
- How many epochs it took
- What hyperparameters mattered
- What broke when you changed them

---

# Part 3 — Break It On Purpose

Intentionally introduce failures.

Examples:
- Forget `model.train()`
- Forget `model.eval()`
- Use too large a learning rate
- Remove gradient zeroing
- Disable shuffling

Observe:
- What changes?
- How do the loss curves look?
- Does validation behave strangely?

Document each failure case in `experiments.md`.

You should understand exactly why each mistake breaks training.

---

# Part 4 — Scaling Sanity Check

Create a slightly larger synthetic dataset.

Train the same model.

Observe:
- Does convergence change?
- Does batch size affect stability?
- Does training time scale predictably?

Document:
- Anything surprising
- Any instability

---

# Required Reflections (Postmortem)

In `postmortem.md`, answer:

1. What does a healthy training curve look like?
2. What does divergence look like?
3. What does overfitting look like?
4. What is the single most important part of your training loop?
5. If your future model fails, where will you look first?

Be concrete. No vague statements.

---

# Completion Criteria

You are done when:

- You can reliably overfit a small dataset.
- You can intentionally cause divergence.
- You can explain every moving piece of your training loop.
- Nothing in the optimization process feels mysterious.

---

# Why This Phase Matters

Every future failure in this curriculum will stress:

- gradients
- optimization
- evaluation
- mode switching
- logging

If Phase 0 is weak, everything else collapses.

Master control now.
