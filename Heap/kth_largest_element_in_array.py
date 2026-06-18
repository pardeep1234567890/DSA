# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?
import heapq
class Solution:
    def findKthLargest(self, nums, k):
        # heapq.heapify(nums)
        # while len(nums) > k :
        #     heapq.heappop(nums)
        # return nums[0] 
        min_heap = []           
        for num in nums :
            heapq.heappush(min_heap,num)
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return min_heap[0]


