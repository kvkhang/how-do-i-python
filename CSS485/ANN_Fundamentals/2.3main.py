import numpy as np
import perceptron as ptron

layer1 = ptron.PerceptronLayer(2, 1, "hardlim")
layer1.print()

p_Train = np.array([[1,4], [1,5], [2,4], [2,5], [3,1], [3,2], [4,1], [4,2]])
t_Train = np.array([[0], [0], [0], [0], [1], [1], [1], [1]])

i = layer1.train(p_Train, t_Train)

print("Iterations: ", i)
print(layer1.print())