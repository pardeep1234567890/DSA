# 1781. Sum of Beauty of All Substrings
# The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.

# For example, the beauty of "abaacc" is 3 - 1 = 2.
# Given a string s, return the sum of beauty of all of its substrings.


# Example 1:

# Input: s = "aabcb"
# Output: 5
# Explanation: The substrings with non-zero beauty are ["aab","aabc","aabcb","abcb","bcb"], each with beauty equal to 1.


def beautySum(self, s):
    max_freq = 0
    min_freq = 0
    total = 0
    for i in range(len(s)):
        freq={}
        for j in range(i,len(s)):
            freq[s[j]] = freq.get(s[j],0)+1
            max_freq = max(freq.values())
            min_freq = min(freq.values())
            beauty = max_freq - min_freq
            total += beauty
    return total 

# we can also solve this problem using the similar format that we used in "Group Anagrams" problem 