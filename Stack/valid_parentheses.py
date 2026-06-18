# def valid_parenthesis(s):
#     stack = []
#     for char in s:
#         if char == "(":
#             stack.append("(")
#         if char == "[":
#             stack.append("[")    
#         if char=="{" :
#             stack.append("{")
#         if char == ")":
#             if stack == []:
#                 return False
#             top_char = stack.pop()
#             if top_char != "(":
#                 return False
#         if char == "]":
#             if stack == []:
#                 return False
#             top_char = stack.pop()
#             if top_char != "[":
#                 return False
#         if char=="}" :
#             if stack == []:
#                 return False
#             top_char = stack.pop()
#             if top_char != "{":
#                 return False
#     if stack == []:
#         return True
#     else: 
#         return False
# print(valid_parenthesis(""))    
# 

def valid_parenthesis(s):
    stack = []
    mapping = {
    ')': '(',
    ']': '[',
    '}': '{'
    }

    for char in s:
        if char in mapping:
            if not stack:
                return False
            top_char = stack.pop()
            if top_char != mapping[char]:
                return False
        else:
            stack.append(char)
    return not stack            
print(valid_parenthesis("}"))            