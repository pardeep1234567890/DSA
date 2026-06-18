# def decode_string(s):
#     stack = []
#     k=0
#     prev_string = ""
#     current_string = ""
#     for i,char in enumerate(s):
#         if "0" <= char <= "9":
#             k = int(char)
#             stack.append(k) 
#         if char == "]":
#             current_string = current_string * k 
#             print(current_string)      
#         if char == "[":
#             prev_string = current_string
#             current_string = current_string+char
#             stack.append(current_string)
  
#         current_string = current_string+char
#     # return current_string


# print(decode_string("3[a]2[bc]"))


def decode_string(s):
    stack = []
    k=0
    prev_string=""
    current_string = ""
    for i,char in enumerate(s):
        if "a" <= char <= "z":
            current_string += char
        if "0" <= char <= "9":
            k = k*10 + int(char)
       
        if char == "[":
            stack.append((current_string,k))
            current_string = ""
            k = 0

        if char == "]":
            prev_string , prev_k= stack.pop()
            current_string = prev_string + current_string *prev_k  
    return current_string


print(decode_string("2[abc]3[cd]ef"))

# Letter   → Add to current_string
# Digit    → Build up k (handles multi-digit numbers)
# [        → Push (current_string, k) to save state, then RESET both
# ]        → Pop (prev_string, prev_k), combine: prev_string + current_string * prev_k