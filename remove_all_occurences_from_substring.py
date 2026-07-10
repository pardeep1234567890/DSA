# Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:
# Find the leftmost occurrence of the substring part and remove it from s.
# Return s after removing all occurrences of part.
# A substring is a contiguous sequence of characters in a string.

def remove_occurrences(s,part):
    stack = []
    k = len(part)
    part_list = list(part)
    for char in s:
        stack.append(char)
        if  len(stack)>= len(part):
            stack_char = stack[-k:]
            if stack_char == part_list:
                del stack[-k:]
    return "".join(stack)
print()