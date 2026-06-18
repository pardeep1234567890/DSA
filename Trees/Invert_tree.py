class TreeNode: 
    def __init__(self,val = 0,left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
class Solution:
    def inverTree(self,root):
        if not root :
            return None
        root.left, root.right = root.right ,root.left
        self.inverTree(root.left)
        self.inverTree(root.right)

        return root