# Concept of the Day: Recursion
# Explanation:Recursion is when a function calls itself to solve a smaller version of the problem.
# The Base Case: The condition to STOP calling itself (otherwise it crashes with "Stack Overflow").
# The Recursive Case: The logic where it calls itself.
# Code (Python - Factorial):Math: $5! = 5 \times 4 \times 3 \times 2 \times 1$Recursive logic: $5! = 5 \times 4!$

def factorial(n):
    # 1. Base Case: Stop at 1
    if n == 1:
        return 1

    # 2. Recursive Case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)


print(factorial(5))
# Logic trace:
# 5 * fact(4)
#   4 * fact(3)
#     3 * fact(2)
#       2 * fact(1) -> Returns 1
# Final: 5*4*3*2*1 = 120