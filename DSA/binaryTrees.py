# Concept of the Day: Binary Trees
# Explanation: A Tree is a hierarchical structure (like a folder system). A Binary Tree is a tree where every node has at most two children (Left and Right).
# Root: The top node.
# Leaf: A node with no children.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Building the Tree:
#      1
#     / \
#    2   3

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(f"Root: {root.value}")       # 1
print(f"Left Child: {root.left.value}") # 2