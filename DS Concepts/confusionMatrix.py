# Concept of the Day: Confusion Matrix
# Explanation: Accuracy can be misleading.
# If 99% of emails are NOT spam, a model that says "Not Spam" for every single email is 99% accurate, but useless (it catches 0 spam).
# A Confusion Matrix breaks down the results:
# True Positive (TP): Predicted Spam, Was Spam. (Good)
# True Negative (TN): Predicted Safe, Was Safe. (Good)
# False Positive (FP): Predicted Spam, Was Safe. (False Alarm)
# False Negative (FN): Predicted Safe, Was Spam. (Missed Detection - Dangerous)

