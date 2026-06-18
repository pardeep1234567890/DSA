import heapq
class ListNode:
    def __init__(self,val= 0,next = None):
        self.val = val
        self.next = next
def merge_k_nodes(lists):
    heap =[]
    dummy = ListNode(0)
    tail = dummy
    for i in range(len(lists)):
        if lists[i] is not None:
            heapq.heappush(heap,(lists[i].val,i,lists[i]))
    while heap:
        val,i,node= heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap,(node.next.val,i,node.next))
    return dummy.next        