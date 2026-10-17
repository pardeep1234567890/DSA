# 137. Single Number II
# Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,3,2]
# Output: 3


def single_number(nums):
    """Return the value that occurs once when every other value occurs thrice."""
    ones = 0
    twos = 0

    for num in nums:
        # Track bit positions seen once and twice modulo three.
        ones = (ones ^ num) & ~twos
        twos = (twos ^ num) & ~ones

    return ones


print(single_number([2, 2, 3, 2]))
