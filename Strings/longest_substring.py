def longest_substring(s):
    window= set()
    left = 0
    max_len=0
    for right in range(len(s)):
        if s[right] in window:
            while s[right] in window:
                window.remove(s[left])
                left += 1
        window.add(s[right])
        max_len = max(max_len, right-left+1)
    return max_len            
print(longest_substring("bbbvbgh")) 

# The problem that I faced while making the brute force approach is how to check whether the character is already repeating or not in your substring. We have to initialise the set to check whether it is already or not. I was thinking that I have to use one more pointer just to compare them. Maybe this is not suitable at all.