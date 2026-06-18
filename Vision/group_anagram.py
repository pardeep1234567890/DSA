# In line 14,15,16 there is whole logic like before that the initial task was make a key 
# and then we set the empty list if key not already exist to group the similar words and if exist then add word to the matching key list 

def group_anagram(strs):
    hash_map = {}
    for word in strs:
        hash_key = [0]*26   # every time it runs again 
        for char in word :
            hash_key[ord(char)-ord("a")] += 1
        key = tuple(hash_key)
        if key not in hash_map:
            hash_map[key] = []
        hash_map[key].append(word)

    return list(hash_map.values())