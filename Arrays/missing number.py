# 268. Missing Number
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array. 
# Example 1:
# Input: nums = [3,0,1]
# Output: 2



# This problem can be solved using sum Formula

def missing_number(nums):
    n = len(nums)
    total_sum = n*(n+1)//2
    given_sum = 0
    for num in nums:
        given_sum += num
    missing_value = total_sum-given_sum
    return missing_value
print(missing_number([3,0,1]))