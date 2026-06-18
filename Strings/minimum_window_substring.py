# def minimum_window_substring(s,t):
#     min_len = float('inf')
#     min_start = 0
#     left = 0
#     freq_map_t ={}
#     formed = 0 # how many characters reached the required frequency 
#     freq_min_window = {} # frequency of required window 
#     result = ""
#     for char in t:
#         freq_map_t[char] = freq_map_t.get(char,0)+1
#     required = len(freq_map_t)   # required is the number of unique characters in the t string
#     for right in range(len(s)):
#         freq_min_window[s[right]] = freq_min_window.get(s[right],0)+1
#         # we only care when the required count is met
#         if s[right] in freq_map_t:
#             if freq_min_window[s[right]] == freq_map_t[s[right]]:
#                 formed += 1      
#         while formed == required:
#             # result += s[left:right+1]  
#             if (right-left+1)<min_len :
#                 min_len = right-left+1
#                 min_start = left 
#             freq_min_window[s[left]] -= 1
#             # freq_min_window.pop(s[left])
#             # if freq_min_window is  reduced then we decrement the counter 
#             if s[left] in freq_map_t:
#                 if freq_min_window[s[left]] < freq_map_t[s[left]]:
#                     formed -= 1
#             left += 1
#     if min_len == float('inf'):
#         return ""    
#     return s[min_start : min_start+min_len]        
            



# print(minimum_window_substring("a","a"))


# i just forget that how to add the string



def minimum_window_substring(s,t):
    min_len = float('inf')
    min_start = 0
    left = 0
    freq_map_t ={}
    formed = 0 
    freq_min_window = {} 
    result = ""
    for char in t:
        freq_map_t[char] = freq_map_t.get(char,0)+1
    required = len(freq_map_t)  
    for right in range(len(s)):
        freq_min_window[s[right]] = freq_min_window.get(s[right],0)+1
        if s[right] in freq_map_t:
            if freq_min_window[s[right]] == freq_map_t[s[right]]:
                formed += 1      
        while formed == required:
            if (right-left+1)<min_len :
                min_len = right-left+1
                min_start = left 
            freq_min_window[s[left]] -= 1
            if s[left] in freq_map_t:
                if freq_min_window[s[left]] < freq_map_t[s[left]]:
                    formed -= 1
            left += 1
    if min_len == float('inf'):
        return ""    
    return s[min_start : min_start+min_len]        
print(minimum_window_substring("ADOBECODEBANC","ABC"))