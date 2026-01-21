# Topic of the Day: Linear Regression (Implementation)
# Explanation: Yesterday we discussed the theory (y = mx + b).
# Today we use Scikit-Learn (the industry standard library) to actually predict values.

import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Prepare Data (2D Array for X is required)
# X = Hours studied, y = Exam Score
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([50, 60, 65, 75, 85])

# 2. Train Model
model = LinearRegression()
model.fit(X, y)

# 3. Predict
# What score will I get if I study 6 hours?
future_X = np.array([[6]])
prediction = model.predict(future_X)

print(f"Prediction for 6 hours: {prediction[0]:.2f}")
print(f"Slope (m): {model.coef_[0]}")
print(f"Intercept (b): {model.intercept_}")