# 1838. Frequency of the Most Frequent Element
# The frequency of an element is the number of times it occurs in an array.
# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
# Return the maximum possible frequency of an element after performing at most k operations.

# Example 1:

# Input: nums = [1,2,4], k = 5
# Output: 3
# Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
# 4 has a frequency of 3.


def maxFrequency(nums, k):
    nums.sort()
    left = 0
    window_sum = 0
    max_freq = 0
    for right in range(len(nums)):
        window_sum = window_sum+nums[right] 
        cost = (right-left+1)*nums[right]-window_sum
        while cost>k :
            window_sum -= nums[left]
            left = left+1
            cost= (right-left+1)*nums[right]-window_sum
        max_freq = max(max_freq,right-left+1)
    return max_freq


