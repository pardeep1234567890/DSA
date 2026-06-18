# Today i learned how to get the key and the values 
# def isomorphic_string(s,t):
#     char_map = {}
#     for i in range(len(s)):
#         if s[i] in char_map:        # i forget that how to access the keys , for that we use the "in" like for existence
#             if char_map[s[i]] != t[i]: # if the value of that char_map[s[i]] is not same then return false
#                 return False
#         else:
#             if t[i] in char_map.values():
#                 return False    
#         char_map[s[i]] = t[i]
#     return True
    

# print(isomorphic_string("ad", "bc"))        



def isomorphic_string(s,t):
    s_t_map = {}
    t_s_map = {}
    for i in range(len(s)):
        if s[i] in s_t_map:       
            if s_t_map[s[i]] != t[i]: 
                return False
        else:
            if t[i] in t_s_map:
                if t_s_map[t[i]] != s[i]:
                    return False   
        s_t_map[s[i]] = t[i]
        t_s_map[t[i]] =s[i] 
    return True
    

print(isomorphic_string("foo", "bar"))        


# Traverse both strings together character by character
# If the current character from the first string has been seen before, verify it maps to the same character in the second string
# If it has not been seen, ensure the current character from the second string is not already mapped by another character
# Store the mapping and continue
# If all characters follow the same mapping rules, return true