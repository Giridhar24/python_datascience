# Topic of the Day: Pivot Tables
# Explanation: If you come from Excel, you know Pivot Tables. They summarize data by reshaping it.
# pivot_table: Unlike groupby (which gives a long list), pivot tables create a grid (matrix) structure, which is often easier to read.

import pandas as pd

df = pd.DataFrame({
    'Product': ['A', 'A', 'B', 'B'],
    'Region': ['North', 'South', 'North', 'South'],
    'Sales': [100, 150, 200, 50]
})

# Goal: Rows = Product, Columns = Region, Values = Sum of Sales
pivot = pd.pivot_table(
    df,
    values='Sales',
    index='Product',
    columns='Region',
    aggfunc='sum'
)

print("--- Pivot Table ---")
print(pivot)
# Result:
# Region   North  South
# Product
# A          100    150
# B          200     50