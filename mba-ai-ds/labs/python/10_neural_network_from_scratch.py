# %% [markdown]
# # Lab 10 · A neural network from scratch (Module M24)
# 🧒 A team of tiny decision-makers. Guess → measure error → pass blame backwards → turn knobs → repeat.
# Task: learn XOR (output 1 only when the two inputs differ). A straight line can't solve it; a network can.

# %% Setup
import numpy as np

rng = np.random.default_rng(0)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([[0], [1], [1], [0]], dtype=float)

# %% 1. The network: 2 inputs → 4 hidden neurons → 1 output
W1, b1 = rng.normal(0, 1, (2, 4)), np.zeros((1, 4))
W2, b2 = rng.normal(0, 1, (4, 1)), np.zeros((1, 1))


def sigmoid(z):
    return 1 / (1 + np.exp(-z))          # squashes any number into 0..1


learning_rate = 1.0

# %% 2. Training loop
for epoch in range(5001):
    # Forward pass: make a guess
    h = sigmoid(X @ W1 + b1)            # hidden layer
    out = sigmoid(h @ W2 + b2)          # output layer
    loss = np.mean((out - y) ** 2)      # how wrong are we?

    # Backward pass: chain rule, blame flows from output back to each weight
    d_out = 2 * (out - y) / len(X) * out * (1 - out)
    d_W2, d_b2 = h.T @ d_out, d_out.sum(axis=0, keepdims=True)
    d_h = d_out @ W2.T * h * (1 - h)
    d_W1, d_b1 = X.T @ d_h, d_h.sum(axis=0, keepdims=True)

    # Gradient descent: step downhill
    W2 -= learning_rate * d_W2; b2 -= learning_rate * d_b2
    W1 -= learning_rate * d_W1; b1 -= learning_rate * d_b1

    if epoch % 1000 == 0:
        print(f"epoch {epoch:5d}  loss {loss:.4f}")

# %% 3. Did it learn?
print("Inputs  → prediction (target)")
for xi, pi, yi in zip(X, out.ravel(), y.ravel()):
    print(f"{xi}  → {pi:.3f}  ({yi:.0f})")

# %% Your turn
# a) Set learning_rate = 0.01. What happens to the loss after 5,000 epochs? (too-small steps)
# b) Set learning_rate = 50. What happens? (too-big steps: jumping over the valley)
# c) Use only 1 hidden neuron (shape (2, 1) and (1, 1)). Can it still learn XOR? Why not?
