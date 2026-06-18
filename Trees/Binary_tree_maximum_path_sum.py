# A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. 
# A node can only appear in the sequence at most once. 
# Note that the path does not need to pass through the root.
# The path sum of a path is the sum of the node's values in the path.
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root):
        max_path = [float("-inf")]
        def path_sum(node):
            if not node: 
                return 0
            # we include 0 because it stop to use of negative numbers
            left = max(path_sum(node.left),0)
            right = max(0,path_sum(node.right))

            sum_of_path = node.val+left +right
            max_path[0] = max(max_path[0],sum_of_path)
            return node.val + max(left,right)
        path_sum(root)    
        return max_path[0]    