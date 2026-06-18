def first_unique_char(s):
    freq_map = {}
    for word in s:
        freq_map[word] = freq_map.get(word,0)+1  
    for i,char in enumerate(s): # i did mistake here that i use freq_map instead of s , because we need index of that string s
        if freq_map[char] == 1:
            return i
    return -1

print(first_unique_char("aabb"))   