# Topic of the Day: Gradient Boosting (XGBoost)
# Explanation: Yesterday we learned Bagging (Random Forests = Parallel Trees).
# Boosting builds trees sequentially.
# Tree 2 fixes the errors of Tree 1.
# Tree 3 fixes Tree 2.
# XGBoost (Extreme Gradient Boosting) is currently the "King of Kaggle"—it is often the winning algorithm for tabular data competitions.

# pip install xgboost
import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split

# Dummy Data
X = np.random.rand(100, 5) # 100 rows, 5 features
y = np.random.randint(0, 2, 100) # Binary target (0 or 1)

# 1. Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# 2. Train XGBoost
# It's fast and handles missing data automatically
model = xgb.XGBClassifier(n_estimators=50, learning_rate=0.1)
model.fit(X_train, y_train)

# 3. Score
accuracy = model.score(X_test, y_test)
print(f"XGBoost Accuracy: {accuracy:.2f}")