# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
class TreeNode: 
    def __init__(self,val = 0,left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
class Solution:
    def same_tree(self,p,q):
        if not p and not q :
            return True
        if not p or not q :
            return False        
        if p.val == q.val:
            if self.same_tree(p.left,q.left) and self.same_tree(p.right,q.right):
                return True 
            else:
                return False       
        else:
            return False 