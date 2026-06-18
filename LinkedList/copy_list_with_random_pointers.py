# we have three phase inside this problem 
# interleave 
# connect the random pointers of the nodes
# separate the list 
class NodeList:
    def __init__(self,val=0,next=None,random = None):
        self.val = val
        self.next = next
        self.random = random 
def copy_list(head):
    if not head:
        return None
    node = head
    original = head
    while node:
        next_node = node.next
        new_node = NodeList(node.val)
        node.next= new_node
        new_node.next = next_node
        node = node.next.next  
    while head:
        if head.random != None:
            head.next.random = head.random.next
        head = head.next.next
    # now seperate the lists 
    copy_head = original.next # i had forget to fix the head of the copy list because we have to return it later so have to save this
    copy_node = copy_head
    while original and original.next :
        # copy_start_node = original.next
        original.next = original.next.next
        if copy_node.next:
            copy_node.next = copy_node.next.next
        original = original.next            #Original: 1 → 2 → [2'] → [3] → [3'] → None
        copy_node = copy_node.next          # Copy:     1' → 2' → [3] → [3'] → None
    return copy_head
            


