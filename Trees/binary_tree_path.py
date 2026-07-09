# Given the root of a binary tree, return all root-to-leaf paths in any order.
# A leaf is a node with no children.

# Example 1:
# Input: root = [1,2,3,null,5]
# Output: ["1->2->5","1->3"]

# 1. using DFS start from first node and initialize a string 
# 2. append the node into string and and if not node then return none
# 3. Undo for tracking the other node 

def binary_tree_path(root):
    result = []
    ans =[]
    def dfs(node):
        if not node:
            return None
        result.append(str(node.val))
        if not node.left and not node.right:
            ans.append("->".join(result))
        else:
            dfs(node.left)
            dfs(node.right)
        result.pop()
    dfs(root)
    return ans
    