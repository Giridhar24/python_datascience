# Concept of the Day: Bit Manipulation (XOR)
#
# Explanation:Computers see 0s and 1s. Bitwise operators work directly on binary.
#
# XOR (^): Returns 1 if bits are different.
# 5 ^ 5 = 0 (Anything XOR itself is 0)
# 5 ^ 0 = 5 (Anything XOR 0 is itself)
#
# Problem: Every number in a list appears twice, except for one.
#
# Find the unique number.
#
# Naive Solution: HashMap (O(N) space).
#
# Bitwise Solution: XOR everything.
# The duplicates cancel out (A XOR A = 0).
# The result is the unique number ($O(1)$ space).


def find_unique(nums):
    result = 0
    for num in nums:
        # XOR the current result with the new number
        result = result ^ num
    return result

numbers = [4, 1, 2, 1, 2]
# Logic:
# 4 ^ 1 ^ 2 ^ 1 ^ 2
# (1^1 is 0), (2^2 is 0) -> we are left with 4 ^ 0 = 4.
print(f"Unique Number: {find_unique(numbers)}")