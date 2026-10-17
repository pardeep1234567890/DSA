# 992. Subarrays with K Different Integers
# Given an integer array nums and an integer k, return the number of good subarrays of nums.
# A good array is an array where the number of different integers in that array is exactly k.
# For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
# A subarray is a contiguous part of an array.
 

# Example 1:

# Input: nums = [1,2,1,2,3], k = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
# Example 2:

# Input: nums = [1,2,1,3,4], k = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


def subarrays_with_k_distinct(nums, k):
    """Return the number of contiguous subarrays containing exactly k values."""
    def at_most(distinct_limit):
        if distinct_limit < 0:
            return 0

        frequencies = {}
        left = 0
        total = 0

        for right, value in enumerate(nums):
            frequencies[value] = frequencies.get(value, 0) + 1

            while len(frequencies) > distinct_limit:
                left_value = nums[left]
                frequencies[left_value] -= 1
                if frequencies[left_value] == 0:
                    del frequencies[left_value]
                left += 1

            total += right - left + 1

        return total

    return at_most(k) - at_most(k - 1)


print(subarrays_with_k_distinct([1, 2, 1, 2, 3], 2))

