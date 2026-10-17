# 2270. Number of Ways to Split Array
# You are given a 0-indexed integer array nums of length n.
# nums contains a valid split at index i if the following are true:
# The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
# There is at least one element to the right of i. That is, 0 <= i < n - 1.
# Return the number of valid splits in nums.

 

# Example 1:

# Input: nums = [10,4,-8,7]
# Output: 2



# def number_of_ways_split_array(nums):
#     count = 0
#     total_sum = sum(nums)
#     left_sum = 0
#     for i in range(len(nums)-1):
#         if i==0:
#             left_sum = nums[i]
#             right_sum = total_sum - left_sum 
#             if right_sum < left_sum:
#                 count += 1
#         else :
#             left_sum = nums[i] + left_sum
#             right_sum = total_sum - left_sum
#             if right_sum < left_sum:
#                 count +=1
#     return count

# print(number_of_ways_split_array([10,4,-8,7]))

def number_of_ways_split_array(nums):
    count = 0
    total_sum = sum(nums)
    left_sum = 0
    for i in range(len(nums)-1):
            left_sum = nums[i] + left_sum
            right_sum = total_sum - left_sum
            if right_sum <= left_sum:
                count +=1
    return count

print(number_of_ways_split_array([10,4,-8,7]))