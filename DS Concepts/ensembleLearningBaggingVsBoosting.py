# Concept of the Day: Ensemble Learning (Bagging vs. Boosting)
# Explanation: How do we combine models?
# Bagging (Bootstrap Aggregating):
# Train models in parallel (independently).
# Each model gets a random subset of data.
# Example: Random Forest.
# Goal: Reduce Variance (Stop overfitting).
# Boosting:
# Train models in sequence (one after another).
# Model 2 focuses on the mistakes made by Model 1. Model 3 focuses on mistakes by Model 2.
# Example: XGBoost, AdaBoost.
# Goal: Reduce Bias (Fix underfitting).

