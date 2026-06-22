# it's all about to know the replacement needed
def longest_repeating_char(s,k):
    left = 0 
    chars_freq = {}
    max_freq = 0
    max_len =0
    # here we expand the window using right variable
    for right in range(len(s)):
        # here we update the freq couunt
        chars_freq[s[right]] = chars_freq.get(s[right],0)+1
        max_freq = max(max_freq,chars_freq[s[right]])
        # here we check the replacment needed > k or not
        while ((right-left+1) -max_freq) > k:
            chars_freq[s[left]] -=1
            left +=1
        max_len = max(max_len,right-left+1)    
    return max_len
print(longest_repeating_char("ABAB",2))

# Exactly right! 👏
# max_freq only grows because we're looking for the longest valid window. A smaller max_freq would only mean we need more replacements for the same window size — that can never beat our current best answer.

# Think of it this way:

# max_freq = 5 means we found a window where one char appeared 5 times → we only need to replace window_size - 5 others
# If max_freq drops to 3, we'd need window_size - 3 replacements → harder to stay within k, so the window can only be equal or smaller
# So max_freq acts like a high watermark — it only matters when it increases, because that's the only time we can potentially find a longer valid window.