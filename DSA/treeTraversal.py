# Concept of the Day: Tree Traversal (DFS)
# Explanation: How do you read every item in a Tree? You can't just loop for i in tree.
# DFS (Depth First Search) goes as deep as possible down one branch before backing up.
# Pre-Order Traversal: Visit Node -> Go Left -> Go Right.

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dfs_preorder(node):
    if node is None:
        return

    # 1. Process Root
    print(node.val, end=" ")

    # 2. Go Left
    dfs_preorder(node.left)

    # 3. Go Right
    dfs_preorder(node.right)


# Tree:
#      1
#     / \
#    2   3
root = Node(1)
root.left = Node(2)
root.right = Node(3)

print("DFS Order:")
dfs_preorder(root)
# Output: 1 2 3