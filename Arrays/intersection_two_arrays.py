# 349. Intersection of Two Arrays
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# def intersection_two_arrays(nums1,nums2):
#     num_set = set()
#     result = []
#     for num in nums1:
#         num_set.add(num)
#     for num in nums2:
#         if num in num_set:
#             result.append(num)
#             num_set.remove(num)
#     return result

# print(intersection_two_arrays([4,9,5],[9,4,9,8,4]))

def intersection_two_arrays(nums1,nums2):
    return list(set(nums1) & set(nums2))

print(intersection_two_arrays([4,9,5],[9,4,9,8,4]))
