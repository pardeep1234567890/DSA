# 2091. Removing Minimum and Maximum From Array
# You are given a 0-indexed array of distinct integers nums.

# There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.

# A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.

# Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.

 

# Example 1:

# Input: nums = [2,10,7,5,4,1,8,6]
# Output: 5
# Explanation: 
# The minimum element in the array is nums[5], which is 1.
# The maximum element in the array is nums[1], which is 10.
# We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
# This results in 2 + 3 = 5 deletions, which is the minimum number possible.

def min_max_remove(nums):
    min_val_idx = nums.index(min(nums)) 
    max_val_idx = nums.index(max(nums)) 

    # i have to find the all strategies 
    both_left_side = max(min_val_idx,max_val_idx)+1
    both_right_side = len(nums)-min(min_val_idx,max_val_idx)
    one_from_each_side = (min(min_val_idx,max_val_idx)+1)+(len(nums)-max(min_val_idx,max_val_idx))

    return min(both_left_side,both_right_side,one_from_each_side)


print(min_max_remove([2, 10, 7, 5, 4, 1, 8, 6]))

# i forget to think about the edge cases 
