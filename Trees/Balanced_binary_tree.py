class TreeNode: 
    def __init__(self,val = 0,left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
# def isBalanced(root):
#     if not root:
#         return True
#     def height(node):
#         if not node :
#             return 0
#         height_node = 1+max(height(node.left),height(node.right))
#         return height_node         
#     return abs(height(root.left) - height(root.right)) <= 1 and isBalanced(root.left) and isBalanced(root.right)

def isBalanced(root):
    def height(node):
        if not node :
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1:
            return -1
        if abs(left-right) > 1: # main role play here 
            return -1
        return 1+max(left,right)
    return height(root) != -1            


# We use max because the height of the tree depends on the 
# maximum depth of nodes, like which goes in the longest node; 
# that will be the height of the tree. That's why we use max.  