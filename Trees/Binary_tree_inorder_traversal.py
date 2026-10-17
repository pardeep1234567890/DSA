# 94. Binary Tree Inorder Traversal
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# def inorder(root):
#     result = []
#     if not root:
#         return result
#     left_node = inorder(root.left)
#     result.append(left_node)
#     result.append(root.val)
#     right_node = inorder(root.right)
#     result.append(right_node)
#     return result

def inorder(root):
    result = []
    if not root:
        return result
    left_node = inorder(root.left)
    result.extend(left_node)
    result.append(root.val)
    right_node = inorder(root.right)
    result.extend(right_node)
    return result
