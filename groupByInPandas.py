# Topic of the Day: GroupBy in Pandas
# Explanation: This is the Python equivalent of SQL's GROUP BY. It involves three steps:
# Split: Break the data into groups based on some criteria (e.g., "Department").
# Apply: Apply a function to each group (e.g., "Sum the salaries").
# Combine: Put the results back into a table.

import pandas as pd

data = {
    'Department': ['Sales', 'Sales', 'HR', 'HR', 'IT'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'Dave', 'Eve'],
    'Salary': [50000, 60000, 45000, 48000, 70000]
}
df = pd.DataFrame(data)

# 1. Group by Department and Calculate Mean Salary
# This answers: "Which department pays the best on average?"
avg_salary = df.groupby('Department')['Salary'].mean()

print("--- Average Salary by Dept ---")
print(avg_salary)

# 2. Multiple Aggregates
# Get the Count AND the Mean
summary = df.groupby('Department')['Salary'].agg(['count', 'mean'])
print("\n--- Detailed Summary ---")
print(summary)