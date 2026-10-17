# 409. Longest Palindrome
# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.


# Example 1:

# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

# def long_pal(s):
#     long = 0 
#     hash_map = {}
#     has_odd = False
#     for char in s:
#         hash_map[char] = hash_map.get(char,0)+1
#     for count in hash_map.values():
#         if count % 2== 0:
#             long += count
#         else :
#             val = count -1
#             long +=val
#             has_odd = True
#     if has_odd :
#         long +=1
#     return long 

    
# print(long_pal("abccccdd"))


def long_pal(s):
    long = 0 
    hash_map = {}
    has_odd = False
    for char in s:
        hash_map[char] = hash_map.get(char,0)+1
    for count in hash_map.values():
        long += count // 2*2
    if long < len(s):
        long +=1 
    return long 

    
print(long_pal("abccccdd"))