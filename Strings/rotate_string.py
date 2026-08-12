# 796. Rotate String
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position.
# For example, if s = "abcde", then it will be "bcdea" after one shift.

def rotate_string(s,goal):
    if len(s) != len(goal):
        return False
    for i in range(len(s)):
        new_string = s[i:] +  s[0:i]
        if new_string == goal:
            return True
    return False
print(rotate_string("abcde","bcdea"))
    