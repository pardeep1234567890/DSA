# You are given an integer array nums and an integer target.
# Return the number of subarrays of nums in which target is the majority element.
# The majority element of a subarray is the element that appears strictly more than half of the times in that subarray.

# My approach 

# I will use the pattern sliding Window because the word subarray justifies that. From that I assume that it uses a sliding Window approach.
# For that I am thinking that I will define two pointers:
# 1. One left
# 2. Second right
# I will traverse the array and check that the current element is the target or not. 
# If it is not the target then move. 
# If the current element is the target then we check that in the current window the target is more than half . if the target is more than half then we increase the count of subarray. 
# Else make it more than half by moving the left pointer and when it becomes more than half then we increase the count.


# my doubt is how to check that it is more than half or not ?
from bisect import bisect_left, insort
def count_subarray_with_majority_element(nums,target):
    for i in range(len(nums)) :
        if nums[i] != target :
            nums[i] = -1
        else :
            nums[i] = 1
    prefix = [0]*len(nums)
    for i in range(len(nums)):
        prefix[i] = prefix[i-1]+nums[i]
    prefix = [0]+prefix
    count = 0
    sorted_list = []
    for val in prefix:
        pos = bisect_left(sorted_list,val)
        count = count +pos
        insort(sorted_list,val)
    return count 

print(count_subarray_with_majority_element([1, 2, 1, 1, 2],1))