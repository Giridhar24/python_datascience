# Topic of the Day: Exploratory Data Analysis (EDA)
# Explanation: Before building models, you must understand your data.
# We use Seaborn (built on Matplotlib) to load practice datasets and visualize relationships instantly.
# Pairplot: Plots every column against every other column.

import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load a built-in dataset (The famous 'Iris' flower dataset)
# Columns: sepal_length, sepal_width, petal_length, petal_width, species
df = sns.load_dataset('iris')

print(df.head())

# 2. The "Pairplot"
# This creates a grid of charts showing correlations between all numbers
# hue='species' colors the dots based on the flower type
sns.pairplot(df, hue='species')

plt.show()