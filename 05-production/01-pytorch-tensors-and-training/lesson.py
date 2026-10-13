"""PyTorch tensors and training: Run a tiny PyTorch regression training loop and observe the loss decrease.

Lesson walkthrough:
    1. Create known data: Use `y = 2x + 1` so expected parameters are known.
    2. Initialize learnable model: `torch.nn.Linear` creates parameters; SGD applies gradient updates.
    3. Repeat optimization: Compute loss, zero gradients, call `backward`, and step the optimizer.

See README.md for concept explanations and a practice task.
"""
import torch

# Optional dependency: pip install -r requirements-deep-learning.txt
torch.manual_seed(42)
X = torch.tensor([[0.0], [1.0], [2.0], [3.0]])
y = 2 * X + 1
model = torch.nn.Linear(1, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
for _ in range(100):
    loss = torch.nn.functional.mse_loss(model(X), y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
print("final loss:", round(loss.item(), 4))
