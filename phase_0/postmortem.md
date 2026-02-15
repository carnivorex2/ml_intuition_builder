# Phase 0 Postmortem

## 1. What does a healthy training curve look like?

A healthy training curve (specifically, the loss curve) typically plummets at the start of training and then flattens out as training progresses. The initial sharp drop signifies that the model is quickly learning the most prominent patterns in the data, while the later flattening indicates a refinement on more subtle patterns or an approach towards the model's performance limit.

## 2. What does divergence look like?

Divergence is when the training loss, instead of decreasing, begins to increase. This often happens rapidly and is a clear sign that the training process is unstable.

## 3. What does overfitting look like?

Overfitting is characterized by the model performing well on the training dataset but poorly on the unseen validation dataset. This is typically observed when the training loss continues to decrease, while the validation loss begins to stagnate or increase.

## 4. What is the single most important part of your training loop?

The most critical part is the coupled process of calculating the gradients and updating the model's weights. `loss.backward()` calculates the gradients, but this is meaningless if the optimizer does not then take a step to update the weights based on those gradients. The two steps form the core learning mechanism.

## 5. If your future model fails, where will you look first?

Based on the experience in Part 4 (Scaling Sanity Check), the first place to look would be the model's architecture. The failure of the model to converge on a slightly larger dataset suggests that the current architecture may not be robust or complex enough to handle more data, making it a primary suspect for future failures.
