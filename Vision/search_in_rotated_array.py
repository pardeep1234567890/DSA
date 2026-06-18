# There is an integer array nums sorted in ascending order (with distinct values),
# which is possibly rotated at an unknown pivot index.

# Given the array nums and an integer target, return the index of target
# if it is in nums, or -1 if it is not in nums.

# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
# Output: 4

# similarly we can use binary search algo 
# initialze the high and low point with last and start index and then find the mid 
# if mid> target then low = mid+1 else high = mid and after complete the loop if we don't find it then return -1 
