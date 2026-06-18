# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root):
        count = 0
        def dfs(max_so_far,node):
            nonlocal count 
            if not node :
                return None 
            if node.val >= max_so_far : 
                count += 1
            max_so_far = max(node.val, max_so_far)
            dfs(max_so_far,node.left)
            dfs(max_so_far,node.right)
        dfs(root.val,root)
        return count 