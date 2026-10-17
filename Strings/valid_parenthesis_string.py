# 678. Valid Parenthesis String
# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
# The following rules define a valid string:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

# def valid_parenthesis(s):
#     stack = []
#     for i in range(len(s)):
#         if s[i] == "(":
#             stack.append(s[i])
#         elif s[i] == ")":
#             stack.pop()
#         elif s[i] == "*":
#             if stack :
#                 top = stack.pop()
#             else:
#                 stack.append("(")
#     if stack:
#         return False 
#     else :
#         return True


# print(valid_parenthesis("(*)"))

def valid_parenthesis(s):
    open_stack = []
    star_stack = []
    for i in range(len(s)):
        if s[i] == "(":
            open_stack.append(s[i])
        elif s[i] == "*":
            star_stack.append(s[i])
        else
    if stack:
        return False 
    else :
        return True


print(valid_parenthesis("(*)"))