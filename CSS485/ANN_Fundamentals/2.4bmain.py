import numpy as np
import perceptron as ptron
import matplotlib.pyplot as plt

layer1 = ptron.PerceptronLayer(30, 3, "hardlim")

# Define the three digit patterns (0, 1, 2) as 1D arrays of length 30.
# Note: The images are stored in row-major order.
zero = np.array([-1,  1,  1,  1,  1, -1,
                  1, -1, -1, -1, -1,  1,
                  1, -1, -1, -1, -1,  1,
                  1, -1, -1, -1, -1,  1,
                 -1,  1,  1,  1,  1, -1])

one = np.array([-1, -1, -1, -1, -1, -1,
                 1, -1, -1, -1, -1, -1,
                 1,  1,  1,  1,  1,  1,
                -1, -1, -1, -1, -1, -1,
                -1, -1, -1, -1, -1, -1])

two = np.array([ 1, -1, -1, -1, -1, -1,
                 1, -1, -1,  1,  1,  1,
                 1, -1, -1,  1, -1,  1,
                -1,  1,  1, -1, -1,  1,
                -1, -1, -1, -1, -1,  1])

# Stack the training patterns into a single array.
p_train = np.array([zero, one, two])

# Create the target outputs as one-hot encoded vectors:
# 0 => [1, 0, 0], 1 => [0, 1, 0], 2 => [0, 0, 1]
t_train = np.array([[1, 0, 0],
                    [0, 1, 0],
                    [0, 0, 1]])

# Train the perceptron with the training patterns.
iterations = layer1.train(p_train, t_train)
print("Training completed in", iterations, "iterations.")
print("Output for Zero:", layer1.forward(zero))
print("Output for One: ", layer1.forward(one))
print("Output for Two: ", layer1.forward(two))

# Function to add noise by flipping a specified number of pixels in the input.
def add_noise(input_array, num_flips):
    # Create a copy of the original input to avoid altering it.
    noisy_array = input_array.copy()
    # Randomly select indices in the input array to flip.
    flip_indices = np.random.choice(len(input_array), num_flips, replace=False)
    for idx in flip_indices:
        noisy_array[idx] = -noisy_array[idx]  # Flip the pixel (i.e., -1 becomes 1 and vice versa)
    return noisy_array

# Generate noisy data for one pattern across various noise levels.
def generate_noisy_data_for_pattern(pattern, noise_levels, num_samples=100):
    noisy_versions = {level: [] for level in noise_levels}
    for level in noise_levels:
        for _ in range(num_samples):
            noisy_versions[level].append(add_noise(pattern, level))
    return noisy_versions

# Evaluate network performance over all patterns and noise levels.
def evaluate_network_on_noisy_data(network, patterns, targets, noise_levels, num_samples=100):
    accuracies = {}
    # Loop over each specified noise level.
    for level in noise_levels:
        correct_count = 0
        total_count = 0
        # Process each training pattern separately.
        for pattern, target in zip(patterns, targets):
            # Generate a set of noisy versions for this pattern at the current noise level.
            noisy_samples = generate_noisy_data_for_pattern(pattern, [level], num_samples)[level]
            for sample in noisy_samples:
                # Pass the noisy sample through the network.
                output = network.forward(sample)
                # Check if the network's prediction matches the target.
                # We use np.argmax to convert the one-hot output into a class label.
                if np.argmax(output) == np.argmax(target):
                    correct_count += 1
                total_count += 1
        # Calculate accuracy (percentage of correctly classified samples).
        accuracy = (correct_count / total_count) * 100
        accuracies[level] = accuracy
    return accuracies

# Define the noise levels (number of pixels flipped).
noise_levels = [2, 4, 6, 8]

# Evaluate the network on the noisy samples generated from each training pattern.
noisy_accuracies = evaluate_network_on_noisy_data(layer1, p_train, t_train, noise_levels, num_samples=100)

# Plot the graph of classification accuracy vs. noise level.
x_values = noise_levels
y_values = [noisy_accuracies[level] for level in noise_levels]

plt.figure(figsize=(8, 6))
plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
plt.title("Classification Accuracy vs. Noise Level")
plt.xlabel("Number of Pixels Flipped (Noise)")
plt.ylabel("Accuracy (%)")
plt.grid(True)
plt.show()

def plot_neuron_weights(weights, num_neurons, input_shape=(6, 5)):
    # Create a subplot for each neuron.
    fig, axes = plt.subplots(1, num_neurons, figsize=(15, 5))
    if num_neurons == 1:
        axes = [axes]  # Ensure axes is iterable even if there's only one neuron.
    
    for i in range(num_neurons):
        # Reshape the neuron's weight vector into the specified image shape.
        weight_matrix = weights[i].reshape(input_shape)
        ax = axes[i]
        # Display the weight matrix as an image using a grayscale colormap.
        ax.imshow(weight_matrix, cmap='gray', vmin=-1, vmax=1)
        ax.set_title(f"Neuron {i+1} Weights")
        ax.axis('off')  # Remove axis ticks for clarity.
    
    plt.tight_layout()
    plt.show()

# Plot the final weights of the perceptron layer.
plot_neuron_weights(layer1.weights, num_neurons=3, input_shape=(6, 5))
