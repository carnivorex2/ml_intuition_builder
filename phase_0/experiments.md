# Phase 0 - Experiments Log

## Part 2: Overfitting Experiment (Synthetic Dataset)

### Objective:
Demonstrate control over the training process by overfitting a small synthetic dataset.

### Findings:

*   **Intermediate Linear Layer Size:** Increasing the size of the intermediate linear layers in the model (`create_model()`) resulted in faster convergence during training.
*   **Learning Rate (LR):** Initial experiments with a high learning rate (e.g., `lr=10`) caused the training process to diverge ("blow up"). A learning rate of `0.01` was found to be stable and allowed for successful convergence.
*   **Training Steps:** The current 20,000 training steps (epochs) were sufficient for the model to reach a state of overfitting, achieving near-zero training loss. It was noted that further convergence might be possible with more training steps.

### Conclusion:
The model successfully overfits the synthetic dataset with a stable learning rate and appropriately sized intermediate layers. The chosen number of training steps effectively demonstrated the ability to reach a near-zero training loss.

## Part 3: Breaking It On Purpose

### Objective:
Intentionally introduce failures into the training process to understand their effects.

### Failure Cases:

*   **Too Large Learning Rate:**
    *   **Action:** Used a significantly large learning rate (e.g., `LR=10`).
    *   **Observation:** The training loss diverged immediately, indicating numerical instability and an inability of the model to learn. This demonstrates the critical role of learning rate in optimization stability.

*   **ReLU After Last Linear Layer:**
    *   **Action:** Added a `nn.ReLU()` activation function after the final `nn.Linear(500, 2)` layer in `create_model()`.
    *   **Observation:** The model stopped learning effectively, and the loss remained high or flat. This is because a ReLU activation can clip negative outputs to zero, which is problematic for the final layer of a classification model (especially with `CrossEntropyLoss` expecting raw logits). The network lost its ability to differentiate between classes effectively due to the non-linearity imposed on the output logits.

## Part 4: Scaling Sanity Check

### Objective:
Train the same model on a slightly larger synthetic dataset to observe changes in convergence and stability.

### Findings:

*   **Dataset Size:** The synthetic dataset size was increased from 100 to 1000 samples.
*   **Convergence:** The model failed to converge on the larger dataset. The validation accuracy was approximately 64%, which is close to the dataset's baseline and indicates the model is not learning the underlying pattern.
*   **Learning Rate:** Adjusting the learning rate did not resolve the convergence issue.
*   **Training Time:** As expected, the training time per step increased significantly due to the larger number of examples being processed in a single batch.

### Conclusion:
The existing model and training configuration, while effective for a very small dataset, is not robust enough to scale to a slightly larger dataset. This highlights a potential issue with the model architecture, optimization method, or the full-batch training approach when faced with more data.