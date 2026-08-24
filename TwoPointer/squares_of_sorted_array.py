# 977. Squares of a Sorted Array
# Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order. 

# Example 1:
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# def square_sorted_array(nums):
#     res = []
#     for num in nums:
#         res.append(num*num)
#     res.sort()
#     return res
# print(square_sorted_array([-4,-1,0,3,10]))

def square_sorted_array(nums):
    res = [0] * len(nums)
    left = 0 
    right = len(nums)-1
    i = len(nums)-1
    while left <= right:
        if abs(nums[right]) > abs(nums[left]):
            res[i] = nums[right]*nums[right]
            i -= 1
            right -=1
        else : 
            res[i] = (nums[left]*nums[left])
            i-=1
            left += 1
    return res
print(square_sorted_array([-4,-1,0,3,10]))