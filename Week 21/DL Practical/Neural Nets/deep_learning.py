import numpy as np

# Define activation functions and their derivatives
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

def initialize_weights(layer_sizes):
    weights = []
    biases = []
    for i in range(len(layer_sizes) - 1):
        W = np.random.randn(layer_sizes[i], layer_sizes[i + 1]) * 0.1
        b = np.zeros((1, layer_sizes[i + 1]))
        weights.append(W)
        biases.append(b)
    return weights, biases

def forward_propagation(X, weights, biases):
    activations = [X]
    Z_values = []

    for i in range(len(weights)):
        Z = np.dot(activations[-1], weights[i]) + biases[i]
        A = sigmoid(Z)
        Z_values.append(Z)
        activations.append(A)

    return Z_values, activations

def backward_propagation(Y, Z_values, activations, weights):
    m = Y.shape[0]
    dZ = activations[-1] - Y
    dWs = []
    dbs = []

    for i in reversed(range(len(weights))):
        dW = np.dot(activations[i].T, dZ) / m
        db = np.sum(dZ, axis=0, keepdims=True) / m
        dWs.insert(0, dW)
        dbs.insert(0, db)

        if i > 0:
            dA = np.dot(dZ, weights[i].T)
            dZ = dA * sigmoid_derivative(activations[i])

    return dWs, dbs

def update_weights(weights, biases, dWs, dbs, learning_rate):
    for i in range(len(weights)):
        weights[i] -= learning_rate * dWs[i]
        biases[i] -= learning_rate * dbs[i]
    return weights, biases

def train_neural_network(X, Y, layer_sizes, epochs, learning_rate):
    # Initialize weights and biases
    weights, biases = initialize_weights(layer_sizes)

    # Training loop
    for epoch in range(epochs):
        # Forward propagation
        Z_values, activations = forward_propagation(X, weights, biases)

        # Compute loss (binary cross-entropy)
        loss = -np.mean(Y * np.log(activations[-1]) + (1 - Y) * np.log(1 - activations[-1]))

        # Backward propagation
        dWs, dbs = backward_propagation(Y, Z_values, activations, weights)

        # Update weights and biases
        weights, biases = update_weights(weights, biases, dWs, dbs, learning_rate)

        # Print loss every 100 epochs
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {loss:.4f}")

    return weights, biases

# Example usage
if __name__ == "__main__":
    # Sample data (XOR problem)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    Y = np.array([[0], [1], [1], [0]])

    # Neural network parameters
    layer_sizes = [2, 4, 4, 1]  # Input layer, 2 hidden layers, output layer
    epochs = 10000
    learning_rate = 0.1

    # Train the neural network
    weights, biases = train_neural_network(X, Y, layer_sizes, epochs, learning_rate)

    # Test the trained network
    _, activations = forward_propagation(X, weights, biases)
    print("Predictions:", activations[-1])
