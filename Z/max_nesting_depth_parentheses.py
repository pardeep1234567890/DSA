# 1614. Maximum Nesting Depth of the Parentheses
# Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses.
 

# Example 1:
# Input: s = "(1+(2*3)+((8)/4))+1"
# Output: 3
# Explanation:
# Digit 8 is inside of 3 nested parentheses in the string.

# 

# def max_depth(s):
#     stack = []
#     for i in range(len(s)):
#         if s[i] == "(":
#             stack.append(s[i])
#         elif s[i] == ")":
#             stack.pop()
#     return len(stack)

# print(max_depth("()(())((()()))"))

# def max_depth(s):
#     stack = []
#     max_len = 0
#     length = 0
#     for i in range(len(s)):
#         if s[i] == "(":
#             stack.append(s[i])
#             max_len = max(len(stack),max_len)
#         elif s[i] == ")":
#             stack.pop()
#     return max_len

# print(max_depth("(1)+((2))+(((3)))"))

def max_depth(s):
    count = 0
    max_len = 0
    for i in range(len(s)):
        if s[i] == "(":
            count += 1
            max_len = max(count,max_len)
        elif s[i] == ")":
            count -=1
    return max_len

print(max_depth("(1)+((2))+(((3)))"))