# Concept of the Day: Valid Parentheses (Stack Problem)
# Explanation: This is a classic interview question. Problem: Given a string like "{ [ ] ( ) }", determine if it is valid.
# Valid: (), ([]), {}[]
# Invalid: (], ([)], ((
# Solution: Use a Stack.
# If you see an Opener (, [, { -> Push to Stack.
# If you see a Closer ), ], } -> Pop from Stack. Does it match?
# Yes? Continue.
# No? Invalid.
# End? Stack must be empty.

def is_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapping:
            # It is a Closer
            # Pop top element (if stack not empty), else assign dummy
            top_element = stack.pop() if stack else '#'

            # Check if it matches the mapping
            if mapping[char] != top_element:
                return False
        else:
            # It is an Opener
            stack.append(char)

    # Return True only if stack is empty
    return not stack


print(is_valid("()[]{}"))  # True
print(is_valid("(]"))  # False