# Topic of the Day: Selecting Data in Pandas (loc vs iloc)
# Explanation: In Pandas, there are two primary ways to select specific rows and columns. Beginners often confuse them:
# loc (Label-based): Select by the name of the row or column.
# iloc (Integer-based): Select by the index number (position), like standard lists (0, 1, 2...).

import pandas as pd

data = {
    'City': ['New York', 'Los Angeles', 'Chicago'],
    'Population': [8000000, 4000000, 2700000]
}
# Setting 'City' as the index (row labels)
df = pd.DataFrame(data).set_index('City')

print("--- Original DataFrame ---")
print(df)

# 1. Using loc (Label)
# "Give me the row for 'Chicago'"
print("\n--- .loc Example ---")
print(df.loc['Chicago'])

# 2. Using iloc (Integer Position)
# "Give me the row at index 1 (which is Los Angeles)"
print("\n--- .iloc Example ---")
print(df.iloc[1])