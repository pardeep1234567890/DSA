# 1658. Minimum Operations to Reduce X to Zero
# You are given an integer array nums and an integer x. In one operation, 
# you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. 
# Note that this modifies the array for future operations.
# Return the minimum number of operations to reduce x to exactly 0 if it is possible, otherwise, return -1.
 

# Example 1:

# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to reduce x to zero.


# input = given an integer array and an integer x
# output - min no. operation  to reduce x to 0 if possible otherwise return 0
 
# we have base case like if the number are greater than x on the both side then return -1
# Either left side or right side 
# we can choose in such that way like either side the value is smaller than x , if both side value are smaller then x 
# then find the larger value (here it can't be done because the thing that is required because we have to make it zero and sometime it is possible with the smaller values) from both of them and subtract from x till 0 and if the value become less than 0 in such way then we return -1


# middle part = total_sum - x

def min_operations(nums,x):
    total_sum = sum(nums)
    target = total_sum -x
    left = 0
    window_sum = 0
    max_len = 0
    # edge cases 
    if total_sum < x:
        return -1
    if total_sum == x or target == 0:
        return len(nums)
    # slide window
    for right in range(len(nums)):
        window_sum += nums[right]
        while window_sum > target:
            window_sum -= nums[left]
            left += 1
        if window_sum == target: 
            max_len = max(max_len,right-left+1)
    # Return Statement
    if max_len != 0:
        return len(nums)-max_len
    else :
        return -1
print(min_operations([1,1,4,2,3],5))