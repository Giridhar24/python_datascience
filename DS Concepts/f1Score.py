# Concept of the Day: F1 Score
# Explanation: Yesterday we debated Precision vs. Recall.
# What if you need both?The F1 Score is the "Harmonic Mean" of Precision and Recall.
# It gives you a single score that balances the two.
# Formula: F1 = 2 * (Precision * Recall) / (Precision + Recall)
# If Precision is 0 or Recall is 0, F1 becomes 0.
# F1 is only high if BOTH Precision and Recall are high.
# Use F1 Score when you have imbalanced classes (e.g., 99% healthy, 1% sick) and you want to beat the "Accuracy Paradox."