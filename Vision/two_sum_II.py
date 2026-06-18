# Given a 1-indexed array of integers numbers that is already
# sorted in non-decreasing order, find two numbers such that
# they add up to a specific target number.

# Return the indices of the two numbers (1-indexed) as an
# integer array answer of length 2, where
# 1 <= answer[0] < answer[1] <= numbers.length.

# You may not use the same element twice and your solution
# must use only constant extra space.

# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: 2 + 7 = 9. index1 = 1, index2 = 2.

#                                   Approach 
# I will use two pointer Approach then the streagy will be 
# Like we move two pointers from one initialised to start and the second initialised to last. 
# We move the pointer from. We add both the pointers and add them. 
# If they are greater than the target then move the right pointer.
#  If they are less than the target then we move the left pointer and return. 
# If it is equal to the target return the index. 

def two_sum(numbers,target):
    left = 0    # i can't initialized to 1 becuase python index start from 0 
    right = len(numbers)-1
    while left<right:
        if numbers[left]+ numbers[right] > target:
            right -=1 
        elif numbers[left]+ numbers[right] < target:
            left +=1
        else:
            return [left+1,right+1]

print(two_sum([2,7,11,15],9))