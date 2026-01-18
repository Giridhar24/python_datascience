# Topic of the Day: Visualization (Matplotlib)
# Explanation: "A picture is worth a thousand rows." Matplotlib is the foundation of plotting in Python.
# plt.plot(): Line chart.
# plt.bar(): Bar chart.
# plt.show(): Displays the graph.

import matplotlib.pyplot as plt

# Data
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
sales = [10, 15, 12, 18, 25]

# 1. Create a simple Line Plot
plt.figure(figsize=(8, 4)) # Set size (width, height)
plt.plot(days, sales, color='blue', marker='o', linestyle='--')

# 2. Add Labels
plt.title("Weekly Sales Growth")
plt.xlabel("Day of Week")
plt.ylabel("Sales ($)")

# 3. Display
plt.show()