# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder,inorder):
        hash_map = {}
        for i in range(len(inorder)):
            hash_map[inorder[i]] = i 
        def maketree(preorder,inorder):
            if not preorder:
                return None 
            root = preorder[0] 
            mid = hash_map[root]
            root_node = TreeNode(root)

            root_node.left = maketree(preorder[1:mid+1],inorder[0:mid])
            root_node.right = maketree(preorder[mid+1:],inorder[mid+1:])
            return root_node
        return maketree(preorder,inorder)


# class Solution:
#     def buildTree(self, preorder,inorder):
#         hash_map = {}
#         for i in range(len(inorder)):
#             hash_map[inorder[i]] = i 
#         def maketree(root,inLeft,inRight):
#             if not inLeft and not inRight:
#                 return None 
#             root = preorder[0] 
#             mid = hash_map[root]
#             root_node = TreeNode(root)

#             root_node.left = maketree(preorder[1:mid+1],inorder[0:mid])
#             root_node.right = maketree(preorder[mid+1:],inorder[mid+1:])
#             return root_node
#         return maketree(preorder,inorder)