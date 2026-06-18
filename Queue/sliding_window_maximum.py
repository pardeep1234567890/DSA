# Remove out-of-window
# Remove smaller elements
# Add current index
# Add max to result

from collections import deque
def sliding_window_max(nums,k):
    queue = deque()
    result = []
    for i in range(len(nums)):
        if queue and queue[0] < i-k+1:  # here start_window = i-k+1 & end_window = i 
            queue.popleft()
        while queue and nums[i] > nums[queue[-1]]:  # why we just append one time and remove until the elements are smaller 
            queue.pop()
        queue.append(i)
        if i >= k-1:
            result.append(nums[queue[0]])
    return result

print(sliding_window_max([1,3,-1,-3,5,3,6,7],3))    