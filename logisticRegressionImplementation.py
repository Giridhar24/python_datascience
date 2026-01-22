# Topic of the Day: Logistic Regression (Implementation)
# Explanation: Yesterday we learned the theory (Sigmoid Curve).
# Today we implement it to predict a Binary outcome (0 or 1).
# Scenario: Predict if a user buys a product (1) or not (0) based on their age.

from sklearn.linear_model import LogisticRegression
import numpy as np

# Data: Age (X) vs Bought? (y)
# Young people (20, 25) didn't buy (0)
# Older people (40, 50) did buy (1)
X = np.array([[20], [25], [40], [50]])
y = np.array([0, 0, 1, 1])

# Train
model = LogisticRegression()
model.fit(X, y)

# Predict for a 30-year-old
age = np.array([[30]])
prediction = model.predict(age)
probability = model.predict_proba(age)

print(f"Prediction (0=No, 1=Yes): {prediction[0]}")
print(f"Confidence: {probability[0]}")
# Output might show ~50% confidence since 30 is in the middle