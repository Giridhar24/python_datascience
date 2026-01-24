# Concept of the Day: Dynamic Programming (Memoization)
# Explanation: Recursion is elegant but can be slow.
# Calculating Fibonacci(50) recursively takes billions of steps because it recalculates the same numbers (Fib(3), Fib(2)) over and over.
# Memoization (Top-Down DP) fixes this by saving the result in a dictionary ("Memo").
# Before calculating, check if we already know the answer.

# Dictionary to store results (The Memo)
memo = {}


def fib_memo(n):
    # 1. Check Memo (Have we solved this before?)
    if n in memo:
        return memo[n]

    # 2. Base Cases
    if n <= 1:
        return n

    # 3. Calculate and SAVE to Memo
    result = fib_memo(n - 1) + fib_memo(n - 2)
    memo[n] = result
    return result


# Standard recursion would freeze here. Memoization is instant.
print(f"Fibonacci(50): {fib_memo(50)}")