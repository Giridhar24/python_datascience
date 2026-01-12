# Explanation: Yesterday we merged tables (joined them sideways based on a key).
# Today we Concatenate (stack them on top of each other).
# This is useful when you have data split across multiple files (e.g., "January Sales", "February Sales") and want one big list.

import pandas as pd

# Data for January
df_jan = pd.DataFrame({
    'Product': ['A', 'B'],
    'Sales': [100, 200]
})

# Data for February
df_feb = pd.DataFrame({
    'Product': ['A', 'C'],
    'Sales': [150, 300]
})

# Stack them vertically (axis=0 is default)
# ignore_index=True resets the row numbers to 0, 1, 2, 3...
full_year = pd.concat([df_jan, df_feb], ignore_index=True)

print("--- Combined Report ---")
print(full_year)