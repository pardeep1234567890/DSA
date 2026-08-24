# 28. Find the Index of the First Occurrence in a String
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, 
# or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

def first_index(haystack,needle):
    """Return the first index of ``needle`` in ``haystack``, or -1."""
    if needle == "":
        return 0

    needle_length = len(needle)
    for start in range(len(haystack) - needle_length + 1):
        if haystack[start : start + needle_length] == needle:
            return start

    return -1



# i was first thinking About hashing after view this problem 
# Then I was thinking about a sliding window Approach 
