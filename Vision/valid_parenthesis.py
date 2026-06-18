# Given a string s containing just the characters
# '(', ')', '{', '}', '[' and ']', determine if the
# input string is valid.

# A string is valid if:
# 1. Open brackets must be closed by the same type of bracket.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket.

# Example 1:
# Input: s = "()"
# Output: True

# Until we have open bracket then push them into the stack.
# When we have the close bracket then we check. 
# We put the brackets from the stack and check if the close bracket and open bracket are the same or not. 
# If they are the same then we move on to check if the stack is empty. Otherwise we will return false.  

def valid_parenthesis(s):
    stack = []
    mapping = {
        "(" : ")",
        "[" : "]",
        "{" : "}"
    }
    for char in s:
        if char in mapping:
            stack.append(char)
        else:
            if not stack :
                return False
            top_stack = stack.pop()
            if mapping[top_stack] != char:
                return False
    if stack:
        return False
    return True            
                
            

