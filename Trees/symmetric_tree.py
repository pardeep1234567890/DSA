# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# from collections import deque

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def symmetric_tree(root):
#         if not root :
#             return True
#         queue = deque([root])
#         root = queue.popleft()
#         queue.append((root.left,root.right))
#         while queue:
#             level_length = len(queue)
#             for _ in range(level_length):
#                 left_node,right_node = queue.popleft()
#                 if not left_node and not right_node :
#                     continue
#                 elif not left_node or not right_node:
#                     return False
#                 elif left_node.val != right_node.val:
#                     return False
#                 queue.append((left_node.left,right_node.right))
#                 queue.append((left_node.right,right_node.left))
#         return True


# Implement the Symmetric Tree Using DFS technique
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def symmetric_tree(root):
        def check_mirror(left_node,right_node):
            if not left_node and not right_node:
                return True
            if not left_node or not right_node :
                return False
            if left_node.val != right_node.val :
                return False
            # if check_mirror(left_node.left,right_node.right) and check_mirror(left_node.right,right_node.left):
            #     return True
            # else :
            #     return False
            return check_mirror(left_node.left, right_node.right) and check_mirror(left_node.right, right_node.left)
        return check_mirror(root.left,root.right)