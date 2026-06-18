# Given an array of integers nums and an integer target, return the indices of the two numbers that add up to target.
# You may assume exactly one solution exists, and you cannot use the same element twice.

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9

def two_sum(nums,target):
    hash_map = {}
    for i in range(len(nums)):
        val = target-nums[i]
        if val in hash_map:
            return [hash_map[val] ,i]
        hash_map[nums[i]] = i 
print(two_sum())