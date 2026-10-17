# 1985. Find the Kth Largest Integer in the Array
# You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.
# Return the string that represents the kth largest integer in nums.
# Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.

 
# Example 1:
# Input: nums = ["3","6","7","10"], k = 4
# Output: "3"
# Explanation:
# The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
# The 4th largest integer in nums is "3".
import heapq
def kth_largest_int(nums,k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap , int(num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return str(min_heap[0])

print(kth_largest_int(["3","6","7","10"], 4))