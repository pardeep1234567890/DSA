# 55. Jump Game
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

def jump_game(nums):
    max_idx = 0
    for i in range(len(nums)):
        if i > max_idx:
            return False
        current_position = nums[i] +i
        max_idx = max(max_idx ,current_position)
        if max_idx>= len(nums)-1:
            return True

    return False
print(jump_game([3,2,1,0,4]))


