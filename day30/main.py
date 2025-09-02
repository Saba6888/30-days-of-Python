#Simple Neural Net with NumPy
import numpy as np

def sigmoid(x): return 1 / (1 + np.exp(-x))

# Inputs and weights
inputs = np.array([0.5, 0.3])
weights = np.array([0.4, 0.6])
bias = 0.1

output = sigmoid(np.dot(inputs, weights) + bias)
print(f"Output: {output:.4f}")



Would you like me to bundle these into a GitHub-ready format or add hoverboard/wireless charging themes to some of them? I can also turn this into a visual README with GIFs and banners if you're planning to showcase it.
