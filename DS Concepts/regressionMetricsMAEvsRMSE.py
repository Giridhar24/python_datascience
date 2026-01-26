# Concept of the Day: Regression Metrics (MAE vs RMSE)
# Explanation: How do we grade a Linear Regression model? Accuracy (%) doesn't work for continuous numbers.
# MAE (Mean Absolute Error): The average difference.
# Example: I predicted $100, actual was $105. Error = 5. Average these errors.
# Pros: Easy to understand ("I am off by $5 on average").
# RMSE (Root Mean Squared Error): Square the errors, average them, then square root.
# Pros: It punishes large errors heavily. Being off by 10 is much worse than being off by 5 twice.
# Rule of Thumb: Use RMSE if big mistakes are unacceptable (e.g., self-driving cars). Use MAE if you just want a general idea.

