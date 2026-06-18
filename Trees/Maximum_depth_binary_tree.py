class TreeNode: 
    def __init__(self,val = 0,left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
class Solution:
    def max_depth(self,root):
        if not root:
            return 0
        maximum = 1+max(self.max_depth(root.left),self.max_depth(root.right)) # the 1 represent the current Node itself depth
        return maximum