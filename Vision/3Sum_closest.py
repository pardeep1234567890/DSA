# Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.


# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).


# there is two options either i should define varibale and check the value is close or not 
# or either check inside the loop 
def three_sum(nums,target):
    nums.sort()  
    result = 0
    best_value = float("inf")
    for i in range(len(nums)-1): 
        left = i+1 
        right = len(nums)-1
        while left<right:
            total = nums[i] + nums[left] + nums[right]
            if best_value > abs(total-target):
                best_value = abs(total-target)
                result = total 
            if total < target :
                left +=1 
            elif total > target :
                right -=1
            else:
                result = total
                return result 

    return result
print(three_sum([-1,2,1,-4],1))