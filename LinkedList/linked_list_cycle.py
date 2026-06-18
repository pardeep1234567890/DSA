def cycle_list(head):
    slow = head
    fast = head
    while fast and fast.next:    # i did also do mistake here that while loop runs only when conditions are true
        slow = slow.next    # i did do the mistake here that i don't update them from there current position
        fast = fast.next.next 
        if fast == slow:
            return True
    return False    