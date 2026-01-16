# Concept of the Day: Linked Lists
# Explanation:An Array stores data side-by-side in memory.
# If you want to insert an item in the middle, you have to shift everyone else over.
# A Linked List stores data scattered in memory.
# Each item (Node) holds:
# Data: The value.
# Pointer (Next): The address of the next node.
# Pros: Fast insertions/deletions ($O(1)$) if you are at the right spot.
# Cons: Slow access ($O(N)$). You can't jump to Index 5; you have to follow the chain: 0 -> 1 -> 2 -> 3 -> 4 -> 5.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # The pointer is initially empty

# Creating the chain: [Head] -> [Second] -> [Third] -> None
head = Node("First")
second = Node("Second")
third = Node("Third")

head.next = second  # Link 1 to 2
second.next = third # Link 2 to 3

# Traversing the list
current = head
while current is not None:
    print(current.data)
    current = current.next