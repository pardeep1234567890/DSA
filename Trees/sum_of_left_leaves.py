# 404. Sum of Left Leaves
# Given the root of a binary tree, return the sum of all left leaves.
# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

# class TreeNode:
#     def __init__(self,val=0,left=None,right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# def sumLeftLeaves(root):
#     if not root and not root.left:
#         return 0
#     total = 0
#     if not root.left and not root.right:
#         return root.val
#     left_val = sumLeftLeaves(root.left)
#     total += left_val
#     return total


class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
def sumLeftLeaves(root):
    if not root:
        return 0
    total = 0
    if root.left and not root.left.left and not root.left.right:
        total += root.left.val
    else :
        total += sumLeftLeaves(root.left)
    total += sumLeftLeaves(root.right)
    return total