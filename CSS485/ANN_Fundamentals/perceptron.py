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
                return ValueError("Bias must be only 1 row")
            self.weights = iw
            self.bias = jb
        
        else:
            return ValueError("Input 2 Scalars or 2 Matrixes")
        
        self.tf = getattr(tf, tfname)
    
    """
    Does a forward pass with the given inputs through a single layer and returns results
    
    Args:
        inputs(np.ndarray): All inputs in one array
    
    Returns:
        output(np.ndarray): All outputs in one array
    """    
    def forwardLoop(self, inputs):
        if (len(inputs) != len(self.weights[0])):
            return ValueError(f"You need {len(self.weights)} inputs")
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
        if (len(inputs) != len(self.weights[0])):
            return ValueError(f"You need {len(self.weights)} inputs")
        output = (self.weights @ inputs) + self.bias
        return self.tf(output)