# 2778. Sum of Squares of Special Elements 
# You are given a 1-indexed integer array nums of length n.
# An element nums[i] of nums is called special if i divides n, i.e. n % i == 0.
# Return the sum of the squares of all special elements of nums.

def sumSqElements(nums):
    n =len(nums)
    total= 0
    for i in range(len(nums)):
        if n % (i+1) == 0:
            total += nums[i]*nums[i]
    return total


print(sumSqElements([1,2,3,4]))