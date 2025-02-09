import numpy as np
import perceptron as ptron

weights = np.array([[1, 1, -1], [-1, -1, 1]])
bias = np.array([0, 0])

ppap = ptron.PerceptronLayer(weights, bias, "hardlim")
print(f"Weights\n{ppap.weights}\nBias\n{ppap.bias}")

print("Outputs for Apple or Pineapple")
print(ppap.forward([1, 1, -1])) # Perfect Apple
print(ppap.forward([-1, -1, 1])) # Perfect Pineapple
print(ppap.forward([1, -1, -1])) # Not Perfect Apple
print(ppap.forward([-1, -1, -1])) # Not Perfect Pineapple