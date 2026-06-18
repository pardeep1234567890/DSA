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