import numpy as np

# Sigmoid activation function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


# Derivative of sigmoid
def sigmoid_derivative(x):
    return x * (1 - x)


# Input data (XOR)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Expected output
y = np.array([
    [0],
    [1],
    [1],
    [0]
])

# Set random seed
np.random.seed(42)

# Initialize weights and biases
input_neurons = 2
hidden_neurons = 4
output_neurons = 1

W1 = np.random.uniform(-1, 1, (input_neurons, hidden_neurons))
b1 = np.zeros((1, hidden_neurons))

W2 = np.random.uniform(-1, 1, (hidden_neurons, output_neurons))
b2 = np.zeros((1, output_neurons))

# Learning rate
learning_rate = 0.5

# Training
for epoch in range(10000):

    # --------------------
    # Forward Propagation
    # --------------------

    hidden_input = np.dot(X, W1) + b1
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W2) + b2
    final_output = sigmoid(final_input)

    # --------------------
    # Backpropagation
    # --------------------

    error = y - final_output

    output_delta = error * sigmoid_derivative(final_output)

    hidden_error = np.dot(output_delta, W2.T)
    hidden_delta = hidden_error * sigmoid_derivative(hidden_output)

    # Update weights and biases
    W2 += np.dot(hidden_output.T, output_delta) * learning_rate
    b2 += np.sum(output_delta, axis=0, keepdims=True) * learning_rate

    W1 += np.dot(X.T, hidden_delta) * learning_rate
    b1 += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate


# Test the trained network
print("Feed Forward Neural Network Output:")
print()

for i in range(len(X)):

    hidden_input = np.dot(X[i:i+1], W1) + b1
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, W2) + b2
    prediction = sigmoid(final_input)

    print(
        "Input:", X[i],
        "Predicted:", round(float(prediction[0][0]), 4),
        "Output:", y[i][0]
    )
