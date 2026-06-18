# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys strictly less than the node's key.
# The right subtree of a node contains only nodes with keys strictly greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

from typing import Optional

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isValidBST(self,root):
#         def check_tree(lower_bound,upper_bound,node):
#             if not node : 
#                 return True
       
#             if lower_bound < node.val < upper_bound:
#                 check_tree(lower_bound,node.val,node.left)
#                 check_tree(node.val , upper_bound , node.right)
#                 return True 
#             else: 
#                 return False
             

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self,root):
        def check_tree(lower_bound,upper_bound,node):
            if not node : 
                return True
       
            if lower_bound < node.val < upper_bound and check_tree(lower_bound,node.val,node.left) and check_tree(node.val , upper_bound , node.right):
                return True 
            else: 
                return False
        return check_tree(float("-inf"),float("+inf"),root)