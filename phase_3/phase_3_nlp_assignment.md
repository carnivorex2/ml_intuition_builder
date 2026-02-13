# Phase 3 Assignment — NLP: Representation vs Sequence

## Core Objective

This phase installs a critical instinct:

> Structure and representation often matter more than model complexity.

You will:
- Build increasingly sophisticated text models.
- Watch simple methods compete with complex ones.
- Learn when sequence modeling actually helps.

This phase is not about large language models.
It is about understanding why they work.

No pretrained transformers.
No external embeddings.
You build from scratch.

---

# Deliverables

Your repository must contain:

- `train.py`
- `models/`
- `experiments.md`
- `postmortem.md`
- Clear documentation of:
  - Tokenization strategy
  - Vocabulary construction
  - Sequence length handling
  - Evaluation metrics

No high-level training frameworks.

---

# Dataset Requirements

Choose a real-world text classification dataset.

Constraints:
- At least 10,000 samples
- Short-to-medium length text (sentences or short documents)
- Supervised classification task

Examples:
- Sentiment analysis
- Topic classification
- Spam detection
- News categorization

Document:
- Average sequence length
- Vocabulary size
- Class distribution

---

# Part 1 — Bag-of-Words Baseline (Mandatory)

Implement a bag-of-words representation:

- Tokenize text
- Build vocabulary
- Represent text as count or TF-based vector
- Train a linear classifier

Record:
- Training loss
- Validation accuracy
- Model size

Document:
- How strong is this baseline?
- Where might it fail?

This baseline is your anchor.

---

# Part 2 — Embeddings + Pooling

Build a model with:

- Learned embeddings
- Mean or max pooling over tokens
- Linear classifier on pooled representation

No recurrence. No attention.

Compare against bag-of-words.

Analyze:
- Does learning embeddings help?
- Does pooling lose critical information?

---

# Part 3 — Sequence Modeling

Implement at least one of:

- RNN (LSTM or GRU)
- 1D CNN over tokens
- Simple attention mechanism

Keep the parameter count reasonable.

Experiment with:
- Sequence length truncation
- Embedding size
- Hidden size
- Depth

Observe:
- Does sequence modeling improve validation performance?
- Does it overfit faster?
- Is it sensitive to hyperparameters?

---

# Part 4 — Data Efficiency Experiment

Train models using:

- 100% of training data
- 50%
- 10%

Compare:
- Performance degradation
- Which model is most data-efficient?

Document:
- Which approach scales best with more data?

---

# Part 5 — Intentional Simplification

Deliberately simplify your best-performing model:

- Reduce embedding size
- Reduce depth
- Remove recurrence or attention

Measure performance change.

Document:
- What complexity was actually necessary?
- What was wasted?

---

# Required Analysis

In `postmortem.md`, answer:

1. How strong was bag-of-words compared to neural models?
2. When did sequence modeling provide real gains?
3. What kinds of errors did each model make?
4. Which model was most stable during training?
5. What tradeoffs exist between simplicity and performance?
6. If forced to deploy a lightweight model, which would you choose?

Be concrete and quantitative.

---

# Completion Criteria

You are done when:

- You understand why bag-of-words is often strong.
- You can explain when order matters in text.
- You can reason about vocabulary size and embedding tradeoffs.
- You no longer assume sequence models automatically win.

---

# Why This Phase Matters

Modern NLP is dominated by transformers.

But transformers solve specific problems:

- Long-range dependency
- Representation learning
- Parallel sequence modeling

If you do not understand what simpler models fail at,
you cannot understand why transformers work.

Learn the failure modes first.
