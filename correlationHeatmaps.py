# Topic of the Day: Correlation Heatmaps
# Explanation: Yesterday we used pairplot. Today we quantify relationships using a Heatmap.
# Correlation Matrix (.corr()): Calculates the mathematical relationship (-1 to 1) between all numerical columns.
# Heatmap: Colors the matrix so you can spot strong relationships (bright colors) instantly.

import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset('iris')

# 1. Calculate Correlation
# Note: We must drop non-numeric columns (like 'species') first
numeric_df = df.drop(columns=['species'])
corr_matrix = numeric_df.corr()

# 2. Plot Heatmap
plt.figure(figsize=(6, 5))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
# annot=True writes the numbers on the boxes
# cmap='coolwarm' makes positive red, negative blue

plt.title("Feature Correlation Matrix")
plt.show()