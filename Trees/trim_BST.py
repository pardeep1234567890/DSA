# Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique answer.
# Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.


# Example 1:
# Input: root = [1,0,2], low = 1, high = 2
# Output: [1,null,2]

def trimBST(root,low,high):
    if not root:
        return None
    if root.val < low :
        return trimBST(root.right,low ,high )
    if root.val > high :
        return trimBST(root.left,low,high)
    if low <= root.val <= high:
        root.left = trimBST(root.left,low,high)
        root.right = trimBST(root.right,low,high)
    return root

# 1. The Core Idea
# When the current root is in bounds (low <= root.val <= high), we know for sure that this current node must remain in the final tree.
# However, even if the current node is valid, some nodes down in its left or right subtrees might still be out of bounds and need to be removed.

# So we must:
# Trim the left subtree.
# Trim the right subtree.
# Re-link the current node to these newly trimmed subtrees.

# That's why we write:
# root.left = trimBST(root.left, low, high)   # Re-link left child to the trimmed left subtree
# root.right = trimBST(root.right, low, high) # Re-link right child to the trimmed right subtree