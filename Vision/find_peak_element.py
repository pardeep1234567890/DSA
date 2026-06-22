# A peak element is an element that is strictly greater than its neighbors.

# Given a 0-indexed integer array nums, find a peak element, and return
# its index. If the array contains multiple peaks, return the index to
# any of the peak elements.

# You may imagine that nums[-1] = nums[n] = -∞. In other words, an element
# is always considered to be strictly greater than a neighbor that is
# outside the array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:
# Input: nums = [1, 2, 3, 1]
# Output: 2

# find peak element then return it's index (element that is stricly greater than it's neighbour)
# how to apply the bionary search if i don't have sorted array 

# Initialize the left and right 
# Find mid and check mid with it's neighbor and move the mid with the side that is greater than mid 
