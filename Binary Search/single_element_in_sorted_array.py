# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
# Return the single element that appears only once.
# Your solution must run in O(log n) time and O(1) space.


# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2


# There is only one specific move like to check that the mid position is even or odd and also check that the mid left element is equal or right element is equal to the mid After that we will check that  mid is even or odd 

def single_element(nums):
    low = 0
    high = len(nums)-1
    while low <= high :
        mid = (low+high)//2
        if mid < len(nums)-1 and nums[mid] == nums[mid+1] :
            if mid%2 == 0 :
                low = mid +1
            else : 
                high = mid -1
        elif mid >0 and nums[mid] == nums[mid-1] :
            if mid%2 ==0 :
                high = mid-1
            else :
                low = mid+1
        else :
            return nums[mid]
print(single_element([3,3,2]))
