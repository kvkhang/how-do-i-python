import transferFunctions as tf
import numpy as np

# For 1d
def singleNeuron(x):
    return tf.hardlim(x - 3)

def neuronLoop(inputs, weights, bias):
    if not isinstance(inputs, np.ndarray) or not isinstance(weights, np.ndarray):
        raise ValueError("Please Input 2 Numpy Arrays")
    if len(inputs) != len(weights) or len(inputs) <= 0:
        raise ValueError("Inputs Must Be Same Length and Greater Than")
    sum = bias
    for x, w in zip(inputs, weights):
        sum += x*w
    return tf.hardlim(sum)

def neuron(inputs, weights, bias):
    if not isinstance(inputs, np.ndarray) or not isinstance(weights, np.ndarray):
        raise ValueError("Please Input 2 Numpy Arrays")
    if len(inputs) != len(weights) or len(inputs) <= 0:
        raise ValueError("Inputs Must Be Same Length and Greater Than 0")
    sum = (inputs @ weights) + bias
    return tf.hardlim(sum)