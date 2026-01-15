# Topic of the Day: The .apply() Method
# Explanation: This is one of the most powerful Pandas features.
# It allows you to "apply" a function to every single row or column in your DataFrame.
# It pairs perfectly with the Lambda functions we just learned.

import pandas as pd

df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Salary': [50000, 60000, 70000]
})

# Scenario: Give everyone a 10% raise
# We apply a lambda function to the 'Salary' column
df['New_Salary'] = df['Salary'].apply(lambda x: x * 1.10)

# Scenario: Extract length of names
df['Name_Length'] = df['Name'].apply(len)

print(df)