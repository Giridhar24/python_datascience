# Topic of the Day: NumPy Array Slicing & Operations
# Explanation: Yesterday we created an array. Today we manipulate it.
# Slicing allows you to grab specific chunks of data (e.g., "rows 1 through 5").
# Broadcasting allows you to do math on the whole array without writing a loop.

import numpy as np

data = np.array([10, 20, 30, 40, 50, 60])

# 1. Slicing: [start_index : stop_index]
# Note: Python stops BEFORE the stop_index.
subset = data[1:4]  # Grabs indices 1, 2, and 3
print(f"Subset (20,30,40): {subset}")

# 2. Built-in Statistical Methods
# No need to write a loop to sum numbers!
print(f"Mean (Average): {data.mean()}")
print(f"Max Value: {data.max()}")

# 3. Filtering
# This creates a boolean mask and filters the data instantly
high_values = data[data > 35]
print(f"Values > 35: {high_values}")