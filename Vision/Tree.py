# Inorder Tree Traversal Example
# Order: Left → Root → Right

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder(node):
    if node is None:
        return
    inorder(node.left)      # Visit left subtree
    print(node.val, end=" ") # Visit root
    inorder(node.right)      # Visit right subtree


# Build a sample tree:
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Inorder Traversal:")
inorder(root)  # Output: 4 2 5 1 3
