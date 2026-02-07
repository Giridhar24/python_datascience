# Concept of the Day: Activation Functions (ReLU vs Sigmoid)
#
# Explanation: Neurons need a filter to decide "Do I fire?"
#
# Sigmoid: S-curve between 0 and 1.
#
# Pros: Good for probability (Output layer).
#
# Cons: Vanishing Gradient problem (Slow learning in deep networks).
#
# ReLU (Rectified Linear Unit): max(0, x). If input is positive, pass it through. If negative, output 0.
#
# Pros: Very fast calculation. No vanishing gradient.
#
# Standard: Use ReLU for almost all hidden layers.