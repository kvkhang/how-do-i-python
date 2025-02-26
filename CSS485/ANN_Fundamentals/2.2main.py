import numpy as np
import perceptron as ptron

layer1 = ptron.PerceptronLayer(2, 1, "hardlim")
layer1.print()

p_Train = np.array([[-1, 1], [-1,-1], [0,0], [1,0]])
t_Train = np.array([[1], [1], [0], [0]])

maxiterations = 100
i = 0
check = True
while check:
    check = False
    for x, t in zip(p_Train, t_Train):
        output = layer1.forward(x)
        error = np.array([layer1.errorLoss(output, t)])
        
        x = np.array(x).reshape(-1, 1)
        
        if (np.sum(error) != 0):
            check = True
            
        errorInput = error.T * x.T
        errorInput = 0.1 * np.append(errorInput, error.T, axis=1)
        layer1.backward(errorInput)
    i += 1
    if (i == maxiterations):
        break

print("Iterations: ", i)
layer1.print()