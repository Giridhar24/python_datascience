# Topic of the Day: K-Means Clustering (Implementation)
#
# Explanation: On Day 14, we learned the theory (grouping data without labels).
#
# Today we implement it. Scenario: We have customer data (Annual Income vs Spending Score).
#
# We want to find distinct customer segments.


from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

# Data: [Income, Spending Score (1-100)]
X = np.array([
    [15, 39], [15, 81], [16, 6], [16, 77], [17, 40], # Low Income
    [70, 40], [75, 50], [80, 45], # Med Income
    [90, 85], [95, 90], [100, 95] # High Income
])

# 1. Train Model (Let's guess 3 clusters)
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# 2. Get Labels (Which group does each person belong to?)
labels = kmeans.labels_
centroids = kmeans.cluster_centers_

print("Labels:", labels)

# 3. Visualize
plt.scatter(X[:,0], X[:,1], c=labels, cmap='rainbow')
plt.scatter(centroids[:,0], centroids[:,1], color='black', marker='X', s=200)
plt.xlabel("Income")
plt.ylabel("Spending Score")
plt.show()