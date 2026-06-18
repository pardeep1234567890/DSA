# class ListNode:
#     def __init__(self,val=0,next = None):
#         self.val = val
#         self.next = next
# def reverse_k_group(head,k):
#     dummy = ListNode(0)
#     dummy.next = head
#     group_prev = dummy
#     # check = group_prev.next
#     # group_start = group_prev.next
#     while True : 
#         # Here we check that K nodes exist or not 
#         check = group_prev 
#         for i in range(k):
#             check = check.next
#             if check is None :
#                 return dummy.next
        
#         # here we will reverse the group
#         # group_prev.next = group_next.next    
#         # group_start = group_prev.next
#         prev = group_prev
#         curr = group_start
#         check.next= group_next # we use it so that we don't lose the remaining list 
#         for i in range(k):   
#             next_node= curr.next
#             prev.next = next_node
#             next_node.next = curr
#             prev = curr
#             curr = curr.next 
#         # after reversing here we will update the pointers    
#         group_next = group_start
#         check = group_prev     

#     return dummy.next


class ListNode:
    def __init__(self,val=0,next = None):
        self.val = val
        self.next = next
def reverse_k_group(head,k):
    dummy = ListNode(0)
    dummy.next = head
    group_prev = dummy
    while True : 
        # Here we check that K nodes exist or not 
        check = group_prev 
        for i in range(k):
            check = check.next
            if check is None :
                return dummy.next
  
        group_start = group_prev.next
        group_next = check.next
        prev = group_next
        curr = group_start
        for i in range(k):   
            next_node= curr.next    # here we use next for just hold
            curr.next = prev
            prev = curr
            curr = next_node 
        group_prev.next =prev  # we update this because now it become reversed now like  1 -> 2 -> 3, =>   3 -> 2 -> 1

        # move to the next group 
        group_prev = group_start
    return dummy.next