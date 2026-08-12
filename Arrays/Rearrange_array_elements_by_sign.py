# 2149. Rearrange Array Elements by Sign
# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

# You should return the array of nums such that the array follows the given conditions:

# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

# def rearrangeArray(nums):
#     result =[0] * len(nums)
#     pos_idx = 0 
#     neg_idx = 1
#     for i in range(len(nums)):
#         if nums[i] > 0:
#             result[pos_idx] = nums[i]
#             pos_idx += 2 
#         else : 
#             result[neg_idx] = nums[i]
#             neg_idx +=2
#     return result

# print(rearrangeArray([3,1,-2,-5,2,-4]))

def rearrangeArray(nums):
    result =[0] * len(nums)
    pos_idx = 0 
    neg_idx = 1
    for num in nums:
        if num > 0:
            result[pos_idx] = num
            pos_idx += 2 
        else : 
            result[neg_idx] = num
            neg_idx +=2
    return result

print(rearrangeArray([3,1,-2,-5,2,-4]))