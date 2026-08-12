# 136. Single Number
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

def single_number(nums):
    result = 0
    for num in nums :
        result = result^num
    return result

print(single_number([4,1,2,1,2]))

# This problem is completely based on one concept , XOR 
# XOR with itself return 0 , XOR with 0 return number itself(ex: 0^4 = 4 , 4^4 = 0)