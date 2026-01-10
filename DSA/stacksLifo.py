# Concept of the Day: Stacks (LIFO)
# Explanation: A Stack is a linear data structure that follows the LIFO (Last In, First Out) principle.
# Analogy: A stack of plates.
# You put a plate on top (Push) and you take the top plate off (Pop).
# You cannot take the bottom plate without removing the top ones first.
# Use Cases: The "Undo" button in text editors, Browser History (Back button).

stack = []

# 1. Push (Add to top)
stack.append("Page 1")
stack.append("Page 2")
stack.append("Page 3")
print(f"Stack: {stack}")

# 2. Pop (Remove from top)
last_item = stack.pop()
print(f"Removed: {last_item}") # Output: Page 3 (The Last one In)

# 3. Peek (Look at top without removing)
print(f"Current Top: {stack[-1]}") # Output: Page 2