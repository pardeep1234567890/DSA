# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
# According to the definition of LCA on Wikipedia:
# “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants 
# (where we allow a node to be a descendant of itself).”
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         current= root
#         while current :
#             # we have three condition to find the lowest common ancestor :
#             # 1. if the value of p and q are less than the  current_node value then move to the left child 
#             # 2. if the value of p and q are  greater then the current_node value then move to the right child 
#             # 3. if the one value from both p and q is less than current value and one value is greater then this will be the split point , we will return that current_value
#             if current.val  < p.val and current.val < q.val :
#                 current = current.right    
#             elif current.val  > p.val and current.val > q.val :
#                 current = current.left
#             else : 
#                 return current 



# Now i will solve this problem using Recursion 
# class Solution:
#     def lowestCommonAncestor(self, root, p, q):
#         if root.val < p.val and root.val > q.val or root.val > p.val and root.val < q.val or root.val == p.val or root.val == q.val :
#             return root
#         if root.val < p.val and root.val < q.val:
#             return self.lowestCommonAncestor(root.right,p,q)
#         if root.val > p.val and root.val > q.val:
#             return self.lowestCommonAncestor(root.left,p,q)
            

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)
        
        return root