# 3550. Smallest Index With Digit Sum Equal to Index
# You are given an integer array nums.
# Return the smallest index i such that the sum of the digits of nums[i] is equal to i.
# If no such index exists, return -1.

# Example 1:
# Input: nums = [1,3,2]
# Output: 2
# Explanation:
# For nums[2] = 2, the sum of digits is 2, which is equal to index i = 2. Thus, the output is 2.


def smallest_idx(nums):
    for i in range(len(nums)):
        total_sum = 0
        x = nums[i]
        while x:
            total_sum += x %10 
            x = x // 10
        if total_sum == i:
            return i
    return -1
print(smallest_idx([1,10,4]))