# 1190. Reverse Substrings Between Each Pair of Parentheses
# You are given a string s that consists of lower case English letters and brackets.
# Reverse the strings in each pair of matching parentheses, starting from the innermost one.
# Your result should not contain any brackets.


# Example 1:

# Input: s = "(abcd)"
# Output: "dcba"
# Example 2:

# Input: s = "(u(love)i)"
# Output: "iloveu"
# Explanation: The substring "love" is reversed first, then the whole string is reversed.

# def reverse_substring_between_parentheses(s):
#     stack = []
#     string = ""
#     for i in range(len(s)):
#         if s[i] == "(" :
#             if len(string) > 0 : 
#                 stack.append(string)
#                 string = ""
#             else :
#                 continue
#         elif s[i] == ")":
#             list_str = list(string)
#             left = 0
#             right = len(list_str)-1
#             while left < right :
#                 list_str[left] , list_str[right]=  list_str[right],list_str[left]
#                 left += 1
#                 right -=1
#             string = "".join(list_str)
#             top_string = stack[-1]
#             stack.append(string +top_string )
#         string += s[i]
#     return stack
        
            


# print(reverse_substring_between_parentheses("(abcd)"))



def reverse_substring_between_parentheses(s):
    stack = []
    string = ""
    for i in range(len(s)):
        if s[i] == "(" :
            stack.append(string)
            string = ""
        elif s[i] == ")":
            top_string = stack.pop()
            rev_string = string[::-1]
            string = top_string + rev_string 
        else:
            string += s[i]
    return string

print(reverse_substring_between_parentheses("(u(love)i)"))


#For now my strategy for solving this problem is: when we look at an open bracket, I'll append the string to the stack 
# and stop appending the string until the next open bracket comes. When I encounter the first close bracket, 
# I will pop the top of the stack string, reverse that string, and append it to the result. 
# The current problem is how the result will be made. 


# Optimized Approach 
def rev_substring(s):
    stack = []
    hashing = {}
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(i)
        elif s[i] == ")":
            top_stack = stack.pop()
            hashing[top_stack] = i
            hashing[i] = top_stack
    i = 0
    direction = 1
    result = ""
    while 0 <= i < len(s):
        if s[i] == "(" or s[i] == ")":
            i = hashing[i]
            direction = - direction 
        else :
            result += s[i]
        i += direction
    return result        



print(rev_substring("(abcd)"))