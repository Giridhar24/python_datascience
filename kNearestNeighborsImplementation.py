# Topic of the Day: K-Nearest Neighbors (Implementation)
# Explanation: Yesterday we learned the theory (voting by neighbors).
# Today we implement it. Scenario: Classify a flower as "Type 0", "Type 1", or "Type 2" based on its measurements.

from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Data: [Petal Length, Petal Width]
X = np.array([[1, 1], [1, 2], [5, 5], [5, 4]])
# Labels: 0 = Small Flower, 1 = Large Flower
y = np.array([0, 0, 1, 1])

# 1. Create Model (K=3)
# It looks at the 3 closest neighbors to decide
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# 2. Predict a new flower [2, 2]
new_flower = np.array([[2, 2]])
prediction = knn.predict(new_flower)

print(f"Class Prediction: {prediction[0]}")
# Likely 0 (Small) because [2,2] is closer to [1,2] than [5,5]