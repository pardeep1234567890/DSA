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