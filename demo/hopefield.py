import numpy as np

def train_hopfield(entries):
    num_entries, num_features = entries.shape

    # Initialize weights matrix
    weights = np.zeros((num_features, num_features))

    # Update weights based on training entries
    for entry in entries:
        weights += np.outer(entry, entry)

    # Set diagonal elements to 0
    np.fill_diagonal(weights, 0)

    return weights

def retrieve_hopfield(test_entry, weights, num_iterations=10):
    retrieved_entry = np.copy(test_entry)

    for _ in range(num_iterations):
        for i in range(len(test_entry)):
            net_input = np.dot(weights[i], retrieved_entry)
            retrieved_entry[i] = 1 if net_input >= 0 else -1

    return retrieved_entry

# Load the dataset from the file
data = np.loadtxt('Dataset\\temp_dataset.txt', dtype=int)

# Extract the two columns from the dataset
entries = data[:, :2]

# Train the Hopfield network
weights = train_hopfield(entries)

# Test the network by retrieving a stored entry
test_entry = entries[0]  # You can choose any entry from the dataset for testing

retrieved_entry = retrieve_hopfield(test_entry, weights)

# Print the retrieved entry
print("Original Entry:", test_entry)
print("Retrieved Entry:", retrieved_entry)
