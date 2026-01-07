# Concept of the Day: Big O Notation
# (Time Complexity)
# Explanation: Before writing complex algorithms, we need a way to measure how "fast" or "slow" they are.
# We don't measure in seconds (because different computers have different speeds).
# We measure by how the number of operations grows as input data ($N$) grows.$O(1)$ - Constant Time: Excellent.
# The speed is the same whether you have 1 item or 1 million items.
# (e.g., Accessing the first element of an array).$O(N)$ - Linear Time: Okay.
# If you double the data, it takes twice as long.
# (e.g., Looping through a list to find a number).$O(N^2)$ - Quadratic Time: Slow.
# If you double the data, it takes 4x as long. (e.g., A loop inside a loop).

# O(1) Example
def check_first(data):
    # Only checks index 0. Always takes 1 step.
    return data[0] == 5

# O(N) Example
def check_all(data):
    # Checks every single item. Takes N steps.
    for item in data:
        if item == 5:
            return True
    return False