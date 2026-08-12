# 1004. Max Consecutive Ones III
# Given a binary array nums and an integer k, 
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

# Example 1:

# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

def max_consecutive_onesIII(nums,k):
    left = 0
    zero_count = 0
    max_window = 0 
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count +=1

        while zero_count > k:
            if nums[left] == 0 :
                zero_count -=1
            left +=1
        max_window = max(max_window,right-left+1)
    return max_window

print(max_consecutive_onesIII([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
            


