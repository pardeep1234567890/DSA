# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.
def permutation_in_strings(s1,s2):
    s1_hash = {}
    window_hash = {}
    if len(s1)>len(s2):
        return False
    for char in s1:
        s1_hash[char] = s1_hash.get(char,0)+1
    for i in range(len(s1)) :
        window_hash[s2[i]] = window_hash.get(s2[i],0)+1
    if s1_hash == window_hash:
        return True
    left = 0
    for right in range(len(s1),len(s2)):
        window_hash[s2[right]] = window_hash.get(s2[right],0)+1
        window_hash[s2[left]] = window_hash.get(s2[left],0)-1
        if window_hash[s2[left]] == 0:
            del window_hash[s2[left]]
        if s1_hash == window_hash:
            return True
        left +=1
    return False

        

    