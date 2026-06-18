def find_all_anagrams(s,p):
    size_p = len(p)
    freq_map_p = {}
    freq_map_s = {}
    left =0
    result = []
    for char in p:
        freq_map_p[char] = freq_map_p.get(char,0)+1
    for right in range(len(s)):
        # here we increase the window size by adding one element and calculate it's frequency
        freq_map_s[s[right]] = freq_map_s.get(s[right],0)+1 # before i did't check i try to add the elements equal to the p length size but instead of that i have to check it later after add characters
        # here we check the window size ,if window size is  greater than the len of p then we reduce from left side 
        while (right-left+1) > len(p): # i did forget that how to check the window size here
            freq_map_s[s[left]] -= 1    
            if freq_map_s[s[left]] == 0:
                freq_map_s.pop(s[left])
            left +=1 
        # here we check the frequency is equal or not (fixed window or len of p string)    
        if freq_map_s  == freq_map_p:
            result.append(left)      
    return result        
print(find_all_anagrams("cbaebabacd", "abc"))


# common example of sliding window 
# for right in range(len(s)):
#     add s[right] to window
#     while window is too big:
#         remove s[left] from window
#         left += 1
#     check condition

#	Mistake	Why It Happened	What To Remember
# 1	Infinite while loop — right wasn't incremented inside the while loop	You confused while with for. The for loop auto-increments, but while doesn't.	✅ If you use a while loop, always ensure the loop variable changes inside the loop to avoid infinite loops.
# 2	Wrong key in .get() — Used right (an index) instead of s[right] (the character)	Copy-paste or mental slip between index and value.	✅ Dictionary keys should be consistent. If you store by character, always access by character, not index.
# 3	Unnecessary inner loop — The while right < len(p) loop inside a for loop	You wanted to build the initial window but overcomplicated it. The for loop already visits every character.	✅ In Sliding Window, one loop is usually enough. Add characters one at a time; don't try to "pre-fill" with an inner loop.
# 4	Wrong order: left += 1 before checking — Incremented left before checking if the count became 0	The order of operations wasn't traced through carefully.	✅ Before writing, trace the code mentally: "What value does left point to now vs after?"
# 5	Wrong method: .pop() on an integer — Called .pop() on freq_map_s[key] instead of freq_map_s.pop(key)	Confusion between dictionary methods and value methods.	✅ dict[key] gives the value. To remove a key, use del dict[key] or dict.pop(key).
# 6	Match check before window adjustment — Checked for anagram before shrinking the window	Didn't simulate the code with an example first.	✅ Order matters! In Sliding Window: 1) Add new element, 2) Shrink if needed, 3) Check condition.
# 7	Missing return statement — Function returned None instead of result	Easy to forget when focused on the algorithm logic.	✅ Always ask: "What should this function return?" and verify it's there.