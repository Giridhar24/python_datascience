# Topic of the Day: Cleaning Data (Renaming & Duplicates)
# Explanation: Data often comes with bad column names ("Column1", "Unnamed: 0") or duplicate rows.
# rename(): Changes column names.
# drop_duplicates(): Removes repeated rows.

import pandas as pd

data = {
    'Col_A': ['Alice', 'Bob', 'Bob', 'Charlie'],
    'Col_B': [25, 30, 30, 35]
}
df = pd.DataFrame(data)

# 1. Rename columns to make them readable
# Syntax: {'Old_Name': 'New_Name'}
df = df.rename(columns={'Col_A': 'Name', 'Col_B': 'Age'})

# 2. Remove Duplicates
# The second 'Bob' row is identical to the first, so it gets removed.
df_clean = df.drop_duplicates()

print("--- Cleaned Data ---")
print(df_clean)