# how to check like zero left 
def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    hash_s = {}
    for char in s:
        hash_s[char] = hash_s.get(char,0)+1
    for char in t :
        if char in hash_s and hash_s[char] != 0:
            hash_s[char] = hash_s.get(char,0)-1
        else :
            return False
    return True