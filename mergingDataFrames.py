# Topic of the Day: Merging DataFrames (pd.merge)
# Explanation: Just like SQL has Joins, Pandas has merge.
# This is how you combine two DataFrames based on a shared column (key).

import pandas as pd

# 1. Create two separate datasets
df_users = pd.DataFrame({
    'id': [1, 2, 3],
    'name': ['Alice', 'Bob', 'Charlie']
})

df_orders = pd.DataFrame({
    'order_id': [101, 102],
    'user_id': [1, 2],  # Note: Charlie (id 3) has no order
    'amount': [250, 400]
})

# 2. Merge them (Inner Join is default)
# "left_on" and "right_on" specify which columns match
merged_df = pd.merge(df_users, df_orders, left_on='id', right_on='user_id', how='inner')

print("--- Merged Data ---")
print(merged_df)
# Charlie will disappear because he is not in the orders table (Inner Join behavior)