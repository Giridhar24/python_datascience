# Concept of the Day: Dynamic Programming (Tabulation)
# Explanation: Yesterday was Memoization (Top-Down).
# We started with the big number (50) and worked down. Tabulation is Bottom-Up.
# We start with 0 and 1, fill a table (array) iteratively up to 50.
# Pro: No recursion limits (Stack Overflow). Usually saves memory.
# Code (Python - Fibonacci Bottom-Up):

def fib_tabulation(n):
    if n <= 1:
        return n

    # 1. Create a table of size n+1
    table = [0] * (n + 1)

    # 2. Set Base Cases
    table[1] = 1

    # 3. Fill the table iteratively
    for i in range(2, n + 1):
        # Current cell = sum of previous two cells
        table[i] = table[i - 1] + table[i - 2]

    return table[n]


print(f"Fib(50): {fib_tabulation(50)}")
# Logic:
# [0, 1, 0, 0...]
# [0, 1, 1, 0...]
# [0, 1, 1, 2...]
# [0, 1, 1, 2, 3...] -> All the way to 50