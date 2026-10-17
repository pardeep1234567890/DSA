# You're given a sorted array of integers where every element appears exactly twice, except for one element that appears exactly once. Find that single element.
# Example: [1, 1, 2, 3, 3, 4, 4, 8, 8] → answer is 2

# Oh, and one more thing — the interviewer adds: "I need this in O(log n) time."

def single_number(nums):
    left = 0
    right = len(nums)-1
    while left<=right:
        mid = (left+right) //2
        if left == right :
            return nums[left ]
        if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
            return nums[mid]
        if mid%2 != 0:
            if nums[mid] == nums[mid+1]:
                right = mid-1
            elif nums[mid] == nums[mid-1]:
                left = mid +1
        else:
            if nums[mid] == nums[mid+1]:
                left = mid +1
            elif nums[mid] == nums[mid-1]:
                right = mid-1
print(single_number([1, 1,2,2, 3, 3, 4, 4,5, 8, 8]))