# Problem 1
# You're given an array that is strictly increasing and then strictly decreasing (a mountain shape). Find the index of the peak element (the maximum).
# Example: [0, 2, 5, 10, 8, 4, 2] → index 3 (value 10)
# O(log n) required.

# Problem 2
# Given an integer array and a target, find three integers whose sum is closest to the target. Return that sum. Exactly one solution is guaranteed.
# Example: [-1, 2, 1, -4], target = 1 → answer is 2 (triplet [-1, 2, 1])

# Problem 3
# Given a sorted array of integers (may include negatives), return an array of the squares of each number, also sorted in non-decreasing order.
# Example: [-4, -1, 0, 3, 10] → [0, 1, 9, 16, 100]
# O(n) required. No library sort.

# Problem 4
# You're given two sorted arrays. The first array has extra space at the end to hold all elements from both arrays. Merge them into the first array, in sorted order, in-place.
# Example: nums1 = [1, 2, 3, 0, 0, 0], m = 3, nums2 = [2, 5, 6], n = 3 → nums1 = [1, 2, 2, 3, 5, 6]
# O(1) extra space.

# Problem 5
# You're given an array. The minimum and maximum elements each need to be removed. You can only remove elements from either end (left or right) of the array, one at a time. Each removal costs 1 operation.
# Find the minimum number of removals needed to delete both the minimum and maximum values.
# Example: [2, 10, 7, 5, 4, 1, 8, 6] → answer is 5
# (Think carefully — you can't just pick the nearest side for each independently.)




# i don't know god what i am currently doing and what happenend with me but it's not happening right
# How could i weak that much 
# i don't want something like that in my life 
# i want to do the hardwork 

# def sorted_array(nums1,nums2):
#     n = len(nums1)
#     m = len(nums2)
#     np = n-m-1
#     mp = m-1
#     k = n-1
#     for i in range(k,-1,-1):
#         if nums1[np] > nums2[mp] and np >= 0:
#             nums1[k] = nums1[np]
#             k -=1 
#             np -=1 
#             if mp == 0 :
#                 break
#         else :
#             if np < 0 :
#                 while mp >=0 and k >= 0:
#                     nums1[k] = nums2[mp]
#                     mp -= 1
#                     k -=1
#             nums1[k] = nums2[mp]
#             k -=1 
#             mp -=1

#     return nums1
        

def sorted_array(nums1,nums2):
    n = len(nums1)
    m = len(nums2)
    p1 = n-m-1
    p2 = m-1
    k = n-1
    while p2 >= 0 and k >= 0:
        if p1 >=0 and nums1[p1]> nums2[p2]:
            nums1[k] = nums1[p1]
            p1 -= 1
            k -=1
        else : 
            nums1[k] = nums2[p2]
            p2 -=1
            k -=1
    return nums1       
print(sorted_array([1,2,3,0,0,0],[2,5,6]))