# Problem 1
# Given an array of size n, find the element that appears more than n/2 times. You may assume such an element always exists.
# Example: [2, 2, 1, 1, 1, 2, 2] → 2
# Constraint: O(1) extra space.

# Problem 2
# Given a sorted array of integers and a target, find the starting and ending position (indices) of the target in the array. If not found, return [-1, -1].
# Example: [5, 7, 7, 8, 8, 10], target = 8 → [3, 4]
# O(log n) required.

# Problem 3
# Given an integer array, rotate it to the right by k steps.
# Example: [1, 2, 3, 4, 5, 6, 7], k = 3 → [5, 6, 7, 1, 2, 3, 4]
# Do it in-place with O(1) extra space.

# Problem 4
# You're given a sorted array that's been rotated, and it may contain duplicates. Given a target, return true if it exists, false otherwise.
# Example: [2, 5, 6, 0, 0, 1, 2], target = 0 → true
# Can you do better than O(n)?

# Problem 5
# Given an array of 2n integers where there are exactly n positive and n negative integers, rearrange them so that positive and negative numbers alternate, starting with positive. Maintain the relative order within positives and within negatives.
# Example: [3, 1, -2, -5, 2, -4] → [3, -2, 1, -5, 2, -4]

def binary_search(nums,target):
    if len(nums) == 0:
        return [-1,-1]
    left = 0 
    right = len(nums)-1
    result = [-1,-1]
    while left <= right :
        mid = (left+right) // 2
        if target == nums[mid]:
            right = mid -1
        elif target < nums[mid]:
            right = mid -1
        else :
            left = mid+1
    if left < len(nums) and nums[left] == target :
        result[0] = left
    low = 0 
    high = len(nums)-1
    while low <= high :
        mid = (low + high) // 2
        if target == nums[mid]:
            low = mid +1
        elif target < nums[mid]:
            high = mid -1
        else :
            low = mid+1 
    if high>=0 and nums[high] == target:
        result[1] = high
    return result
print(binary_search([5,7,7,8,8,10],8))
        

