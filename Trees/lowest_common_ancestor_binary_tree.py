def lowestCommonAncestor(root, p, q):
    if not root:
        return None 
    if root.val == p.val or root.val == q.val: # if we find any p or q firstly on the top then we don't need to look at the decendents because it we be on their left or right side 
        return root
    left_node = lowestCommonAncestor(root.left,p,q)
    right_node = lowestCommonAncestor(root.right,p,q)

    if left_node and right_node:
        return root
    if left_node and not right_node:
        return left_node
    if not left_node and right_node:
        return right_node
    return None