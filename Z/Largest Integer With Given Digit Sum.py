# Q1. Largest Integer With Given Digit Sum
# Easy
# 3 pt.
# You are given two non-negative integers n and s.

# Return the largest integer that has at most n digits and whose sum of digits is s. If no such integer exists, return -1.

#  

# Example 1:

# Input: n = 2, s = 9

# Output: 90

# Explanation:

# The largest integer with at most 2 digits that has a sum of digits of 9 is 90.

def largest_sum(n,s):
    if s==0:
        return 0 
    if s > (n*9):
        return -1
    result = []
    for i in range(n):
        digit = min(9,s)
        result.append(str(digit))
        s = s-digit
        
    return int("".join(result))
print(largest_sum(3,10))

