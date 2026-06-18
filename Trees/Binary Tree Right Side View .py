# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        queue = deque([root])
        result = []
        if not root:
            return []
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                level_node = queue.popleft()
                if level_node.left:
                    queue.append(level_node.left)
                if level_node.right: 
                    queue.append(level_node.right)    
                if i == level_length-1:
                    result.append(level_node.val)
        return result          