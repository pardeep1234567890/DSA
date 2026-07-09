# Given the root of a binary tree, return the length of the diameter of the tree.
# The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
# The length of a path between two nodes is represented by the number of edges between them.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_binary_tree(root):
    longest_diameter = 0
    def height(node):
        nonlocal longest_diameter
        if not node :
            return 0 
        left_height = height(node.left)
        right_height = height(node.right)
        diameter = left_height + right_height
        longest_diameter = max(diameter,longest_diameter)
        return 1+ max(left_height,right_height)
    height(root)
    return longest_diameter

    # def diameter_binary_tree(root):
    # def height(node):
    #     if not node :
    #         return (0,0)
    #     left_height,left_diameter = height(node.left)
    #     right_height,right_diameter = height(node.right)
    #     diameter = left_height + right_height
    #     longest_diameter = max(diameter,left_diameter,right_diameter)
    #     return (1+ max(left_height,right_height),longest_diameter)
    # height , long_diameter = height(root)
    # return long_diameter