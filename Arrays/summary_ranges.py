# 228. Summary Ranges
# You are given a sorted unique integer array nums.
# A range [a,b] is the set of all integers from a to b (inclusive).
# Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Each range [a,b] in the list should be output as:

# "a->b" if a != b
# "a" if a == b
 

# Example 1:

# Input: nums = [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: The ranges are:
# [0,2] --> "0->2"
# [4,5] --> "4->5"
# [7,7] --> "7"


# def summary_ranges(nums):
#     result = []
#     if len(nums) == 1:
#         result.append(str(nums[0]))
#     start = 0
#     range_nums = 0 
#     for i in range(len(nums)-1):
#         if nums[i+1] - nums[i] != 1:
#             if nums[start] != nums[i]:
#                 range_nums = str(nums[start]) + "->" + str(nums[i])
#             else:
#                 range_nums = str(nums[start])
#             start = i+1
#             result.append(range_nums)
#             # range_nums = 0
#         if i==len(nums)-2:
#             if nums[start] == nums[i+1]:
#                 range_nums = str(nums[start])
#             else : 
#                 range_nums = str(nums[start]) + "->" + str(nums[i+1])
#             result.append(range_nums)
#     return result

# print(summary_ranges([5]))


def summary_ranges(nums):
    result = []
    i = 0
    # start = 0
    range_num = 0
    while i < len(nums):
        start = i
        while i+1<len(nums) and nums[i+1] - nums[i] ==1:
            i +=1
        if nums[start] == nums[i]:
            range_num = str(nums[start])
        else:    
            range_num = str(nums[start]) + "->" + str(nums[i])
        result.append(range_num)
        i = i+1
    return result
print(summary_ranges([0,2,4,5,7]))
