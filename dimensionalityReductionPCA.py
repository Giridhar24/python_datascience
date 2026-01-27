# Topic of the Day: Dimensionality Reduction (PCA)
#
# Explanation: What if you have a dataset with 50 columns? It's hard to visualize and slow to train.
#
# PCA (Principal Component Analysis) squashes those 50 columns down to 2 or 3 "Principal Components" (Super-columns) that retain most of the information.
#
# It allows you to plot complex data on a 2D screen.

from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

# Load Data (4 columns: Sepal Length, Width, Petal Length, Width)
data = load_iris()
X = data.data
y = data.target

# 1. Reduce from 4D to 2D
pca = PCA(n_components=2)
X_2d = pca.fit_transform(X)

print(f"Original Shape: {X.shape}") # (150, 4)
print(f"New Shape: {X_2d.shape}")   # (150, 2)

# 2. Visualize the Compressed Data
plt.scatter(X_2d[:, 0], X_2d[:, 1], c=y, cmap='viridis')
plt.title("Iris Data Compressed to 2 Dimensions")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.show()