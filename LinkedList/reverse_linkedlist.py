class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev






















#----------------------------------------------------------#
# Helper function to print linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

# Create nodes with correct values
s1 = Node(10)
s2 = Node(20)
s3 = Node(30)

# Link the nodes together
s1.next = s2
s2.next = s3

print("Original list:")
print_linked_list(s1)

# Reverse the linked list
reversed_head = reverse_list(s1)

print("Reversed list:")
print_linked_list(reversed_head)