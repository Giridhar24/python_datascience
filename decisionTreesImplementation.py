# Topic of the Day: Decision Trees (Implementation)
# Explanation: A Decision Tree is like a flowchart.
# It asks a series of Yes/No questions to classify data.
# It is highly interpretable (you can visualize exactly why the model made a decision).

from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Data: [Experience, Written Score] -> Hired? (0=No, 1=Yes)
X = [[1, 50], [2, 60], [5, 80], [6, 85]]
y = [0, 0, 1, 1]

# 1. Train
model = DecisionTreeClassifier()
model.fit(X, y)

# 2. Visualize the Logic
plt.figure(figsize=(6, 4))
plot_tree(model, feature_names=['Experience', 'Score'], class_names=['No', 'Yes'], filled=True)
plt.show()

# The tree will show something like:
# "If Experience <= 3.5, Class = No"
# "If Experience > 3.5, Class = Yes"