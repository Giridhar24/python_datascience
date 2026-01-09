# Topic of the Day: Handling Missing Data (dropna & fillna)
# Explanation: Real-world data is messy. You will often find NaN (Not a Number) or null values. You usually have two choices:
# Drop: Delete the rows with missing data (if you have plenty of data).
# Impute (Fill): Fill the holes with the average (Mean) or 0 (if you need to preserve data quantity).

import pandas as pd
import numpy as np

# Creating data with missing values (np.nan)
data = {'Score': [100, 90, np.nan, 95],
        'Name': ['Alice', 'Bob', 'Charlie', 'Dave']}
df = pd.DataFrame(data)

print("--- Original ---")
print(df)

# Option 1: Drop rows with ANY missing value
clean_drop = df.dropna()
print("\n--- After Dropping ---")
print(clean_drop)

# Option 2: Fill missing values with the average score
mean_val = df['Score'].mean()
clean_fill = df.fillna(mean_val)
print("\n--- After Filling (Imputation) ---")
print(clean_fill)