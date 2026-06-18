# Given the root of a binary search tree, and an integer k,
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


class Solution:
	def kthSmallest(self, root, k):
            count_list = [0]
            result =[0]
            def kthValue(node,k):
                if not node:
                    return None
                if count_list[0] >= k:
                    return None
                kthValue(node.left,k)
                count_list[0] += 1
                if count_list[0] == k :
                    result[0] = node.val 
                kthValue(node.right,k)
            kthValue(root,k)    
            return result[0]         


# class Solution:
# 	def kthSmallest(self, root, k):
# 		count_list = [0]
#         result = 0
#         def kthValue(node,k):
#             if not node:
#                 return None
#             if kthValue(node.left) and kthValue(node) and kthValue(node.right): # sorry i remembered it when i written it 
#                 count_list[0] +=1
#                 if count_list[0] == k :
#                     return node.val
#         return kthValue(root,k)

#         # i did it in the same way like written them in the different lines