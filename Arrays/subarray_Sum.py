# 2104. Sum of Subarray Ranges
# You are given an integer array nums. The range of a subarray of nums is the difference between the largest and smallest element in the subarray.
# Return the sum of all subarray ranges of nums.
# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0 
# [2], range = 2 - 2 = 0
# [3], range = 3 - 3 = 0
# [1,2], range = 2 - 1 = 1
# [2,3], range = 3 - 2 = 1
# [1,2,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 1 + 1 + 2 = 4.
# Example 2:

# Input: nums = [1,3,3]
# Output: 4
# Explanation: The 6 subarrays of nums are the following:
# [1], range = largest - smallest = 1 - 1 = 0
# [3], range = 3 - 3 = 0
# [3], range = 3 - 3 = 0
# [1,3], range = 3 - 1 = 2
# [3,3], range = 3 - 3 = 0
# [1,3,3], range = 3 - 1 = 2
# So the sum of all ranges is 0 + 0 + 0 + 2 + 0 + 2 = 4.

def subArrayRanges(nums):
    range_sum = 0
    for i in range(len(nums)):
        largest_num = nums[i]
        smallest_num = nums[i]
        for j in range(i,len(nums)):
            if nums[j] > largest_num :
                largest_num =nums[j]
            if nums[j] < smallest_num:
                smallest_num = nums[j]
            range_sum += largest_num - smallest_num
    return range_sum
print(subArrayRanges([4,-2,-3,4,1]))