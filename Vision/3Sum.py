# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that i != j, i != k,
# j != k, and nums[i] + nums[j] + nums[k] == 0.

# The solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# the brute force is like that : i will traverse the array and add the three number and make combinations list of the pairs whose sum is equal to Zero 

# def three_sum():
#     nums = [-1,0,1,2,-1,-4]
#     result = []
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             for t in range(j+1,len(nums)):
#                 if nums[i]+ nums[j]+ nums[t] == 0 and sorted([nums[i], nums[j], nums[t]]) not in result:
#                     result.append(sorted([nums[i],nums[j],nums[t]]))
#     return result
# print(three_sum())


def three_sum(nums):
    nums.sort()  
    result = []
    for i in range(len(nums)-1):
        if i>0 and nums[i] == nums[i-1]:
            continue 
        left = i+1 
        right = len(nums)-1
        while left<right:
            total = nums[i] + nums[left] + nums[right]
            if total< 0 :
                left +=1 
            elif total > 0 :
                right -=1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left <right and nums[left] == nums[left+1]:
                    left+=1
                while left < right and nums[right] == nums[right-1]: 
                    right -=1
                left +=1
                right -=1
    return result
print(three_sum( [-2, 0, 0, 0, 2, 2]))