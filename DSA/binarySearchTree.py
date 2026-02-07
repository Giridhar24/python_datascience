# Concept of the Day: Binary Search Tree (BST)
#
# Explanation:A BST is a sorted tree.
#
# Rule: For any node, everything in the Left subtree is smaller.
#
# Everything in the Right subtree is larger.
#
# Benefit: Search, Insert, and Delete are all O(log N) on average.


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, key):
    # 1. If tree is empty, return new node
    if root is None:
        return Node(key)

    # 2. If key is smaller, go Left
    if key < root.val:
        root.left = insert(root.left, key)
    # 3. If key is larger, go Right
    else:
        root.right = insert(root.right, key)

    return root


# Building BST: 50 -> 30 -> 20 -> 40 -> 70 -> 60 -> 80
root = Node(50)
insert(root, 30)
insert(root, 20)
insert(root, 40)
insert(root, 70)
insert(root, 60)
insert(root, 80)