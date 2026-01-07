# Topic of the Day: Introduction to Pandas DataFrames
# Explanation: While NumPy is for math, Pandas is for structured data (like Excel sheets).
# The core object is the DataFrame—a table with rows and columns.
# It is the most important tool in a Python Data Scientist's toolkit.

import pandas as pd

# 1. Creating data (usually a dictionary of lists)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}

# 2. Converting to a DataFrame
df = pd.DataFrame(data)

# 3. Inspecting the data
print("--- Full Table ---")
print(df)

print("\n--- Select Single Column ---")
print(df['Name'])

# 4. Basic Info
# .describe() gives quick stats (count, mean, min, max) for numeric columns
print("\n--- Quick Stats ---")
print(df.describe())