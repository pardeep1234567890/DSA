class TreeNode: 
    def __init__(self,val = 0,left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
def isSubtree(root,subroot):
    if not root :
        return False 
    def isIdentical(root_node,subroot_node):
        if not root_node and not subroot_node:
            return True
        if not subroot_node:
            return False
        if not root_node:
            return False 
        if root_node.val != subroot_node.val :
            return False 
        return (isIdentical(root_node.left, subroot_node.left) and isIdentical(root_node.right, subroot_node.right))   
    return(isIdentical(root,subroot) or isSubtree(root.left , subroot) or isSubtree(root.right,subroot))