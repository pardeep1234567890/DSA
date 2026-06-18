class ListNode:
    def __init__(self,val=0,next = None):
        self.val = val
        self.next = next
def reorder_list(head):
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Here we want to split the Linked list 
    second_half = slow.next 
    slow.next = None
    curr = second_half
    prev = None             # i did just forget to use prev , we have to use it and it's a cruical point 
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node 
    # now the task is to merge the list 
    dummy = ListNode(0) 
    tail = dummy
    l1 = head
    l2 = prev
    while l1 and l2 :
        tail.next = l1
        l1 = l1.next
        tail = tail.next 
        tail.next = l2
        l2 = l2.next
        tail = tail.next
    if l1 :
        tail.next = l1
    return dummy.next        