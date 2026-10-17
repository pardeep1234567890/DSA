# 1876. Substrings of Size Three with Distinct Characters
# A string is good if there are no repeated characters.
# Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
# Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
# A substring is a contiguous sequence of characters in a string.


# Example 1:

# Input: s = "xyzzaz"
# Output: 1
# Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
# The only good substring of length 3 is "xyz".

# def substring_of_size_three(s):
#     hash_map = {}
#     for i in range(2):
#         hash_map[s[i]] = hash_map.get(s[i],0)+1
#     left = 0
#     count = 0
#     for right in range(2,len(s)):
#         hash_map[s[right]] = hash_map.get(s[right],0)+1
#         if all(v==1 for v in hash_map.values()) :
#             count +=1
#         hash_map[s[left]] = hash_map.get(s[left],0)-1
#         if hash_map[s[left]] == 0:
#             del hash_map[s[left]]
#         left += 1
#     return count 
# print(substring_of_size_three("abcxyz"))