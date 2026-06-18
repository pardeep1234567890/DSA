# Given a string s, find the length of the longest substring without repeating characters.
# i will use the approach longest sliding window 
# I will use two pointers, first left and right. Move right will go until the 

def long_substring(s):
    left = 0
    set_s = set()
    long_sub = 0 
    for right in range(len(s)):
        if s[right] in set_s :
            while s[right] in set_s:
                set_s.remove(s[left])
                left +=1 
        long_sub = max(long_sub,right-left+1)   
        set_s.add(s[right])
    return long_sub

print(long_substring("abcabcbb"))