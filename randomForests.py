# Topic of the Day: Random Forests
# Explanation: Yesterday we built a Decision Tree.
# The problem is, a single tree is prone to errors (High Variance).
# A Random Forest builds 100 different trees (using random subsets of data) and asks them to vote.
# Logic: "The wisdom of the crowd." If 80 trees say "Yes" and 20 say "No", the answer is "Yes".

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
import numpy as np

# Load Data
data = load_iris()
X, y = data.data, data.target

# 1. Create Model
# n_estimators=100 means "Build 100 trees"
model = RandomForestClassifier(n_estimators=100)

# 2. Train
model.fit(X, y)

# 3. Feature Importance
# Random Forests are great at telling you WHICH column matters most
importances = model.feature_importances_
print(f"Feature Importances: {importances}")
# Output will show 4 numbers. Higher number = More important feature.