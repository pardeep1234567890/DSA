# when i was soving this problem , i was thinking in the wrong way like do every steps in different step 
# and also i did forget to increment the pointers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def merge_sorted_list(list1,list2):
    l1 = list1
    l2 = list2 
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            tail = tail.next
            l1 = l1.next
        else:
            tail.next = l2
            tail = tail.next
            l2 = l2.next
    if l1:
        tail.next = l1 
    if l2:
        tail.next = l2               
    return dummy.next       