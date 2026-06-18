class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
        
def add_numbers(l1,l2):
    carry = 0
    dummy = ListNode(0)
    current = dummy
    while l1 or l2 or carry:
        if l1 :
            val1 = l1.val
            l1 = l1.next        # i forget to move the pointers
        else:
            val1 = 0    
        if l2 :
            val2 = l2.val
            l2 = l2.next
        else:
            val2 =0         
        sum = val1+val2+carry
        new_Node = ListNode(sum%10)
        carry = sum//10
        current.next = new_Node
        current = new_Node
    return dummy.next    