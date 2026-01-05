# Topic of the Day: Introduction to NumPy Arrays

# Explanation: Data Science in Python relies heavily on a library called NumPy.
# Standard Python lists are slow for heavy math.
# NumPy provides the ndarray (n-dimensional array), which is up to 50x faster. Today, we simply create an array.

import numpy as np

# Standard Python List
py_list = [1, 2, 3, 4, 5]

# Convert to NumPy Array
np_array = np.array(py_list)

# Why it matters: Vectorization
# You can multiply the whole array at once (impossible with standard lists)
doubled_array = np_array * 2

print(f"Original List: {py_list}")
print(f"Numpy Array:   {np_array}")
print(f"Doubled:       {doubled_array}")
print(f"Shape of array: {np_array.shape}") # Tells you dimensions (5,)