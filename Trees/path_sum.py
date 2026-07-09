class TreeNode: 
    def __init__(self,val = 0,left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

def path_sum(root,target_sum):
    def check_sum(node , remaining):
        if not node :
            return False
        remaining = remaining - node.val 
        if not node.left and  not node.right:
            if remaining == 0 :
                return True
        if check_sum(node.left,remaining) or check_sum(node.right,remaining):
            return True
        return False
    return check_sum(root,target_sum)
    