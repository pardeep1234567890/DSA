# 1248. Count Number of Nice Subarrays
# Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
# Return the number of nice sub-arrays.

# Example 1:

# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example 2:

# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There are no odd numbers in the array.
# Example 3:

# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16


# def count_nice_suarrays(nums,k):
#     total_odd_subarray = 0
#     odd_count = 0
#     left = 0
#     for right in range(len(nums)):
#         if nums[right] % 2 != 0:
#             odd_count += 1
#         if odd_count == k :
#             total_odd_subarray +=1 
#         while odd_count > k :
#             if nums[left] % 2 != 0 :
#                 odd_count -=1 
#             left += 1
#     return total_odd_subarray
# print(count_nice_suarrays([1,1,2,1,1],3))



def count_nice_subarrays(nums,k):
    # total_odd_subarray = 0
    # odd_count = 0
    # left = 0
    def count_odd_subArray(nums,k):
        left = 0 
        odd_count = 0  
        total_count = 0  
        for right in range(len(nums)):
            if nums[right] % 2 != 0:
                odd_count += 1
            while odd_count > k :
                if nums[left] % 2 != 0 :
                    odd_count -=1 
                left += 1
            if odd_count <= k:
                total_count += right-left+1 
        return total_count
    return count_odd_subArray(nums,k)-count_odd_subArray(nums,k-1)

print(count_nice_subarrays([1,1,2,1,1],3))