def longest_palindrome_substring(s):
    pal_string = ""
    for i in range(len(s)):
        left = i-1
        right = i+1
        while left>=0 and right<len(s) and s[left] == s[right]:
            left -= 1
            right +=1 
        if len(pal_string) < len(s[left+1:right]):
            pal_string = s[left+1:right]    
        left = i 
        right = i+1    
        while left>=0 and right<len(s) and s[left] == s[right]:
            left -= 1
            right +=1    
        if len(pal_string) < len(s[left+1:right]):
            pal_string = s[left+1:right]        
    return pal_string

print(longest_palindrome_substring("a"))