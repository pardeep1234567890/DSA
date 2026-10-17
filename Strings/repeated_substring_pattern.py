# 459. Repeated Substring Pattern
# Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

# Example 1:

# Input: s = "abab"
# Output: true
# Explanation: It is the substring "ab" twice.
# Example 2:

# Input: s = "aba"
# Output: false

# two pointer , sliding window , hashing , set 
# So i was not thinking in the way of Length , i was thiking in way of Frequency 

# Brute Force Approach
# def repeated_substring_pattern(s):
#     N = len(s)
#     L = N//2
#     for i in range(1,L+1):
#         if N%i ==0:
#             sub_len = s[:i]*(N//i)
#             if sub_len == s:
#                 return True
#     return False


# print(repeated_substring_pattern("abab"))


# Optimized Approach
def repeated_substring_pattern(s):
    doubled = s+s
    modified = doubled[1:-1]
    if s in modified:
        return True
    else :
        return False
print(repeated_substring_pattern("abab"))