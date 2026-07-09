class TreeNode: 
    def __init__(self,val = 0,left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

# def path_sum(root,target_sum):
#     result =[]
#     def check_sum(node,remaining,curr_node_list):
#         if not node :
#             return False
#         remaining = remaining-node.val
#         curr_node_list.append(node.val)
#         if not node.left and not node.right:
#             if remaining == 0 :
#                 result.append(curr_node_list[:])
#                 curr_node_list.pop()
#                 return
#         check_sum(node.left,remaining,curr_node_list)
#         check_sum(node.right,remaining,curr_node_list)
#         curr_node_list.pop()
#     check_sum(root,target_sum,[])
#     return result
    
def path_sum(root,target_sum):
    result =[]
    def check_sum(node,remaining,curr_node_list):
        if not node :
            return False
        remaining = remaining-node.val
        curr_node_list.append(node.val)
        if not node.left and not node.right:
            if remaining == 0 :
                result.append(curr_node_list[:])
        else:
            check_sum(node.left,remaining,curr_node_list) 
            check_sum(node.right,remaining,curr_node_list)
        curr_node_list.pop()
    check_sum(root,target_sum,[])
    return result
    