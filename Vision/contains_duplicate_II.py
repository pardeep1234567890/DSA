# Given an integer array nums and an integer k, 
# return true if there are two distinct indices i and j in the array 
# such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:

# Input: nums = [1,2,3,1], k = 3
# Output: true

# here is the approach is simple to optimize the Approach we use hashmap so that we can remember past values
# so we store the values in the hashmap where key is the array integer and value is the index because we want to check that i-j<=k or not 
# if it satisfies the condition then we return true else after complete the array the we return false

#                                       thinking :
# The more recent index is always closer to any future occurrence. 
# If index 0 couldn't satisfy the condition with index 2, it definitely won't satisfy it with index 3, 4, etc. either (the distance only grows). So keeping the older index is pointless — the newer one gives you the best chance of satisfying abs(i - j) <= k in the future.