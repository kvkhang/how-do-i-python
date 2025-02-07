import numpy as np
import perceptron as ptron

weights = np.array([[0.5, 0.5], [1, 1]])
bias = np.array([-1, -1])

gates = ptron.PerceptronLayer(weights, bias, "hardlim")
print(f"Weights\n{gates.weights}\nBias\n{gates.bias}")

print("Outputs for And/Or Gates")
print(gates.forward([0,0]))
print(gates.forward([1,0]))
print(gates.forward([0,1]))
print(gates.forward([1,1]))