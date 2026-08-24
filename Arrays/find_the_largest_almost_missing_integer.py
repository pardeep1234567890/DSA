# 3471. Find the Largest Almost Missing Integer
# You are given an integer array nums and an integer k.
# An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.
# Return the largest almost missing integer from nums. If no such integer exists, return -1.
# A subarray is a contiguous sequence of elements within an array.
 

# Example 1:
# Input: nums = [3,9,2,1,7], k = 3
# Output: 7

# Explanation:
# 1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
# 2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
# 3 appears in 1 subarray of size 3: [3, 9, 2].
# 7 appears in 1 subarray of size 3: [2, 1, 7].
# 9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
# We return 7 since it is the largest integer that appears in exactly one subarray of size k.

# def almost_largest_missing_integer(nums,k):
#     largest_value = float("-inf")
#     n = len(nums)
#     hash_value = {}
#     for num in nums:
#         hash_value[num] = hash_value.get(num,0)+1
#     if k ==1:
#         for number in nums:
#             if number > largest_value and hash_value[number] <= 1:
#                 largest_value = number
#         return largest_value
#     if k ==n:
#         return max(nums)
#     else :
#         if hash_value[nums[0]] <= 1 and nums[0] > nums[n-1]:
#             return nums[0]
#         elif hash_value[nums[n-1]] <= 1 and nums[0] < nums[n-1]:
#             return nums[n-1]
#     return -1


# print(almost_largest_missing_integer([0,0],1))

def almost_largest_missing_integer(nums,k):
    n = len(nums)
    hash_value = {}
    for num in nums:
        hash_value[num] = hash_value.get(num,0)+1
    result = -1
    if k ==1:
        for number in nums:
            if hash_value[number] == 1:
                result = max(result,number)
        return result
    elif k ==n:
        return max(nums)
    else :
        if hash_value[nums[0]] == 1 and hash_value[nums[n-1]] ==1:
            return max(nums[0],nums[n-1])
        elif hash_value[nums[0]] == 1 and hash_value[nums[n-1]] !=1:
            return nums[0]
        elif hash_value[nums[n-1]] ==1 and hash_value[nums[0]] !=1:
            return nums[n-1]
        else :
            return result
    return result


print(almost_largest_missing_integer([0,0],1))