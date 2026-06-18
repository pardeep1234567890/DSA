# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
from collections import deque
class TreeNode: 
    def __init__(self,val = 0,left=None, right=None):
        self.val = val
        self.right = right
        self.left = left
class Codec:
    def serialize(self, root):
        # I serialize the tree using preorder traversal and include null markers to preserve structure.
# Preorder DFS traversal (root → left → right)
# Appends str(node.val) for real nodes, "Null" for missing nodes
# Returns a comma-separated string like
        queue = deque()
        def dfs(node):
            if not node:
                queue.append("Null")
                return None
            # Like we are using preorder so we first Process the Node then recursively calling the left subtree then and right Subtree    
            queue.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(queue)

    def deserialize(self, queue):
        def built():
            val = queue.popleft()
            if val == "Null":
                return None
            root = TreeNode(int(val)) 
            root.left = built()
            root.right = built()
            return root
        queue = deque(queue.split(","))    
        return built()