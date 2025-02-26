import numpy as np
import perceptron as ptron
import matplotlib.pyplot as plt

layer1 = ptron.PerceptronLayer(30, 3, "hardlim")

zero = np.array([-1, 1, 1, 1, 1, -1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, 1, -1, 1, 1, 1, 1, -1,])
one = np.array([-1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
two = np.array([1, -1, -1, -1, -1, -1, 1, -1, -1, 1, 1, 1, 1, -1, -1, 1, -1, 1, -1, 1, 1, -1, -1, 1, -1, -1, -1, -1, -1, 1])

p_train = np.array([zero, one, two])
t_train = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

print(layer1.forward(zero))

i = layer1.train(p_train, t_train)
print("Iterations: ", i)
print(layer1.forward(zero))
print(layer1.forward(one))
print(layer1.forward(two))

def plot_neuron_weights(weights, num_neurons, input_shape=(6, 5)):

    fig, axes = plt.subplots(1, num_neurons, figsize=(15, 5))
    
    if num_neurons == 1:
        axes = [axes]  # Make it iterable if there's only one axis
    
    for i in range(num_neurons):
        # Reshape the weight vector of the ith neuron into a 5x6 matrix
        weight_matrix = weights[i].reshape(input_shape)
        # Plot the weight matrix as a grayscale image
        ax = axes[i]
        ax.imshow(weight_matrix, cmap='gray', vmin=-1, vmax=1)  # Use grayscale colormap
        ax.set_title(f"Neuron {i + 1}")
        ax.axis('off')  # Hide axes for better visualization
    
    plt.tight_layout()
    plt.show()

plot_neuron_weights(layer1.weights, num_neurons=3)

