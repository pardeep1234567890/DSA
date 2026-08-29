# 316. Remove Duplicate Letters
# Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"

def remove_letters(s):
    hash_map = {}
    stack = []
    char_set = set()
    for i in range(len(s)):
        hash_map[s[i]] = i
    for i in range(len(s)):
        if s[i] not in char_set :
            while stack and s[i] < stack[-1] and i<hash_map[stack[-1]]:
                char = stack.pop()
                char_set.remove(char)
            stack.append(s[i])
            char_set.add(s[i])
    return "".join(stack)
print(remove_letters("bcabc"))

# Hash map → {char: last_index} — to know if a character appears later
# Stack → to build the result, popping larger characters when a smaller one arrives
# Set → to skip characters already in the stack

# ----------------------------------------------------------------------------------------------------------------
# Yes I was very sure that this is a similar kind of problem, like removing duplicate numbers at all. I have also solved previously, like removal element and others. They use two pointers but I know this problem doesn't use it.
# Secondly I was thinking of the pattern to solve this problem using hashing and using the order function but the problem statement is something else. I was wrong then AI gave me a hint to help me in such a case. 
# This is the stack problem. When I was reading the hint at the start, I was thinking about the pattern. Maybe it would be a dynamic programming or greedy kind of pattern but it was not. Also help me to check how to identify the greedy or DP kind of patterns. 
# I would like to request you, anti-gravity AI, to please help me in such a case.    wait....
# this problem is actually greddy 