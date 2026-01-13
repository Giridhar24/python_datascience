# Topic of the Day: CSV Handling (read_csv & to_csv)
# Explanation: Data Scientists rarely write raw text files. We work with CSV (Comma Separated Values) files. Pandas makes this trivial.
# pd.read_csv(): Loads a file into a DataFrame.
# df.to_csv(): Saves a DataFrame to a file.

import pandas as pd

# 1. Create a quick DataFrame
df = pd.DataFrame({
    'Student': ['Alice', 'Bob', 'Charlie'],
    'Grade': [88, 92, 79]
})

# 2. Save to CSV
# index=False tells Pandas NOT to save the row numbers (0, 1, 2)
df.to_csv("grades.csv", index=False)
print("File 'grades.csv' saved!")

# 3. Read it back
loaded_df = pd.read_csv("grades.csv")
print("\n--- Loaded Data ---")
print(loaded_df)