# Concept of the Day: Tree Traversal (BFS)
# Explanation: Yesterday was DFS (Depth First - go deep). Today is BFS (Breadth First Search) - go wide.
# BFS visits the tree layer-by-layer: Level 1 (Root), then all of Level 2, then all of Level 3.
# Tool Required: A Queue (FIFO).

from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs_traversal(root):
    if not root:
        return

    queue = deque([root])  # Start with root in queue

    while queue:
        # 1. Remove from front
        current = queue.popleft()
        print(current.val, end=" ")

        # 2. Add children to back
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


# Tree:
#      1
#     / \
#    2   3
root = Node(1)
root.left = Node(2)
root.right = Node(3)

print("BFS (Level Order):")
bfs_traversal(root)
# Output: 1 2 3