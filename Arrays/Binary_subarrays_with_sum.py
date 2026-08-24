# 930. Binary Subarrays With Sum
# Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.
# A subarray is a contiguous part of the array.

# Example 1:
# Input: nums = [1,0,1,0,1], goal = 2
# Output: 4
# Explanation: The 4 subarrays are bolded and underlined below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]

# def binary_subarray_sum(nums,goal):
#     left = 0
#     count = 0
#     sum = 0
#     for right in range(len(nums)):

#         sum += nums[right]
#         if sum == goal:
#             count += 1 
#         while sum > goal and left < right:
#             sum-=nums[left]
#             left +=1
#             while sum == goal and left < right:
#                 count +=1
#                 sum-= nums[left]
#                 left += 1
#     return count 
# print(binary_subarray_sum([0,0,0,0,0], 0))

# def binary_subarray_sum(nums,goal):
#     left = 0
#     count = 0
#     sum = 0
#     for right in range(len(nums)):

#         sum += nums[right]
#         if sum == goal:
#             count += 1 
#         while sum > goal and left < right:
#             sum-=nums[left]
#             left +=1
#             while sum == goal and left < right:
#                 count +=1
#                 sum-= nums[left]
#                 left += 1
#         while left != right and right == len(nums)-1:
#             left +=1
#             sum-= nums[left]
#             if sum == goal:
#                 count +=1 
#     return count 
# print(binary_subarray_sum([0,0,0,0,0],0))




def binary_subarray_sum(nums,goal):
    if goal <0 :
        return 0 
    def count_at_most(nums,goal):
        left = 0
        sum = 0
        count = 0
        for right in range(len(nums)):
            sum += nums[right]
            while sum > goal and left < right:
                sum-=nums[left]
                left +=1
            if sum <= goal :
                count += right-left+1
        return count 
    return count_at_most(nums,goal) - count_at_most(nums, goal-1)
print(binary_subarray_sum([0,0,0,0,0],0))
