# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if not root : 
            return []
        queue = deque([root])
        result = []
        while queue : 
            level_length = len(queue)
            level = []
            for _ in range(level_length):
                queue_node = queue.popleft()
                if queue_node.left:
                    queue.append(queue_node.left)
                if queue_node.right:
                    queue.append(queue_node.right)
                level.append(queue_node.val)    
            result.append(level)
        return result         




# while = level-by-level driver
# for = node-by-node processor within a single level