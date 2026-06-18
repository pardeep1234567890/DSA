# Given the root of a binary tree, invert the tree, and return its root.
def invert_tree(root):
    if not root:
        return
    invert_tree(root.left)
    invert_tree(root.right)
    root.left , root.right = root.right , root.left 
    return root