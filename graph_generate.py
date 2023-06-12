import matplotlib.pyplot as plt
import numpy as np

data_x = []
data_y = []

with open('facebook_combined.txt', 'r') as file:
    for line in file:
        x, y = line.strip().split(' ')
        data_x.append(float(x))
        data_y.append(float(y))

# Convert the data to NumPy arrays (optional but useful for manipulation)
data_x = np.array(data_x)
data_y = np.array(data_y)

# Create the figure and axes
fig, ax = plt.subplots()

# Plot the data
ax.plot(data_x, data_y)

# Customize the plot (optional)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_title('Graph')

# Show the plot
plt.show()

