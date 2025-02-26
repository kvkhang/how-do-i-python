import numpy as np
import transferFunctions as tf


class PerceptronLayer:
    """
    A single Perceptron Layer
    """

    """
    Creates a Perceptron Layer from either predetermined or random weights

    Args:
        iw(int or np.ndarray): inputs/weight matrix
        jb(int or np.ndarray): outputs/bias matrix
        tfname(string): sets the transfer function type
    """

    def __init__(self, iw, jb, tfname):
        if isinstance(iw, int) and isinstance(jb, int):
            self.weights = np.random.uniform(-1, 1, size=(jb, iw))
            self.bias = np.random.uniform(-1, 1, size=(jb))

        elif isinstance(iw, np.ndarray) and isinstance(jb, np.ndarray):
            if len(jb) != len(iw):
                raise ValueError("Bias must be only 1 row")
            self.weights = iw
            self.bias = jb

        else:
            raise ValueError("Input 2 Scalars or 2 Matrixes")

        self.tf = getattr(tf, tfname)

    """
    Does a forward pass with the given inputs through a single layer and returns results
    
    Args:
        inputs(np.ndarray): All inputs in one array
    
    Returns:
        output(np.ndarray): All outputs in one array
    """

    def forwardLoop(self, inputs):
        if len(inputs) != len(self.weights[0]):
            raise ValueError(f"You need {len(self.weights)} inputs")
        output = np.zeros(len(self.bias))
        i = 0
        for weights, b in zip(self.weights, self.bias):
            for w, x in zip(weights, inputs):
                b += w * x
            output[i] = self.tf(b)
            i += 1
        return output

    """
    Does a forward pass with the given inputs through a single layer and returns results
    
    Args:
        inputs(np.ndarray): All inputs in one array
    
    Returns:
        output(np.ndarray): All outputs in one array
    """

    def forward(self, inputs):
        if len(inputs) != len(self.weights[0]):
            raise ValueError(f"You need {len(self.weights)} inputs")
        output = (self.weights @ inputs.T) + self.bias
        return self.tf(output)
    
    def errorLoss(self, a, t):
        if len(a) != len(t):
            raise ValueError("Length MisMatch")
        return t - a

    def backward(self, errors):
        if (errors.ndim == 1):
            if len(errors) != (len(self.weights[0]) + 1):
                raise ValueError(f"You need {len(self.weights)} inputs")
        elif len(self.weights) > 1:
            if len(errors) != len(self.weights):
                raise ValueError(f"You need {len(self.weights)} by {len(self.weights[0])} inputs")
        for x in range(len(errors)):
            self.bias[x] += errors[x][-1]
        if errors.ndim == 1:
            errors = np.delete(errors, -1)
        else:
            errors = np.delete(errors, -1, axis=1)
        self.weights += errors

    def print(self):
        print("Layer:")
        i = 1
        for x, b in zip(self.weights, self.bias):
            print(f"   W{i} = {x}\tb = {b}")
            i += 1

    def train(self, p_Train, t_Train):
        if (len(p_Train) < 2):
            raise ValueError("Must pass in more than 2 values")
        if (len(p_Train) != len(t_Train)):
            raise ValueError("Both vectors must have the same amount of answers")
        i = 0
        check = True
        while check:
            check = False
            for x, t in zip(p_Train, t_Train):
                output = self.forward(x)
                error = np.array([self.errorLoss(output, t)])
                
                x = np.array(x).reshape(-1, 1)
                
                if (np.sum(error) != 0):
                    check = True
                    
                errorInput = error.T * x.T
                errorInput = 0.1 * np.append(errorInput, error.T, axis=1)
                self.backward(errorInput)
            i += 1
        return i