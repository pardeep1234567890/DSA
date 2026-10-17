# 450. Delete Node in a BST
# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
# Basically, the deletion can be divided into two stages:
# Search for a node to remove.
# If the node is found, delete the node.

class TreeNode:
    def __init__(self,val=0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
def Delete_node_BST(root,key):
    if not root:
        return None
    if root.val < key :
        root.right = Delete_node_BST(root.right,key)
    elif root.val > key:
        root.left = Delete_node_BST(root.left,key)
    else:
        if not root.left and not root.right:
            return None
        elif not root.right:
            # root.val = root.right.val
            return root.left
        elif not root.left:
            # root.val = root.left.val
            return root.right
        else:
            successor = root.right
            while successor.left:
                successor = successor.left

            root.val = successor.val
            root.right = Delete_node_BST(root.right,successor.val)

    return root
    