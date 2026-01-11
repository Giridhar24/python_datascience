# Concept of the Day: Queues (FIFO)
# Explanation: A Queue is a linear data structure that follows the FIFO (First In, First Out) principle.
# Analogy: A line at a ticket counter. The first person to join the line is the first person to get a ticket.
# Key Operations:
# Enqueue: Add item to the back.
# Dequeue: Remove item from the front.

# While lists work, 'collections.deque' is faster for queues in Python
from collections import deque

queue = deque()

# 1. Enqueue (Add to right/back)
queue.append("Person A")
queue.append("Person B")
queue.append("Person C")
print(f"Queue: {queue}")

# 2. Dequeue (Remove from left/front)
served = queue.popleft()
print(f"Served: {served}")    # Output: Person A (First In)

print(f"Next in line: {queue[0]}") # Output: Person B