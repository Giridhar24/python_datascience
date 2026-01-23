# Concept of the Day: K-Fold Cross Validation
# Explanation: Train/Test split (80/20) is good, but risky.
# What if the 20% you hid contained all the weird/hard examples? Your accuracy score would be fake. K-Fold Cross Validation:
# Split data into K parts (e.g., 5).
# Train on parts 1-4, Test on 5.
# Train on parts 2-5, Test on 1.
# Repeat 5 times.
# Take the average score. This is a much more honest accuracy rating.
