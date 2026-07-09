# You are given two strings s and t consisting of lowercase English letters.
# You may choose at most one index in s and replace the character at that index with any lowercase English letter.
# Return true if it is possible to make s a subsequence of t; otherwise, return false.

# Example 1:
# Input: s = "cat", t = "chat"
# Output: true

# Explanation:
# Replace s[1] from 'a' to 'h'. The resulting string is "cht".
# "cht" is a subsequence of "chat" because we can match 'c', 'h', and 't' in order.

# def canMakeSubsequence(self, s, t):
#     def isSubseq(wildcard_idx):
#         i = 0
#         j = 0 
#         while i < len(s) and j < len(t):
#             if s[i] == t[j] or i == wildcard_idx:
#                 i +=1
#                 j+=1
#             else:
#                 j+=1
#         if i == len(s):
#             return True
#         else:
#             return False
#     if isSubseq(-1):
#         return True
#     for idx in range(len(s)):
#         if isSubseq(idx):
#             return True
#     return False  

def canMakeSubsequence(self, s, t):
    match0 = 0
    match1 = 0
    for char in t :
        next_match0 = match0
        if match0 < len(s) and s[match0] == char:
            next_match0 = match0+1
        next_match1 = match1
        if next_match1 <len(s) and s[match1] == char:
            next_match1 = max(next_match1,match1+1)
        if match0 <len(s):
            next_match1 = max(next_match1,match0+1)
        match0 = next_match0
        match1 = next_match1
    if match1 == len(s):
        return True
    else:
        return False


              
