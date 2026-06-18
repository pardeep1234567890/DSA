def group_anagrams(strs):
    anagram_map = {}
    for word in strs:
        freq = [0]*26
        for char in word:   
            freq[ord(char) - ord('a')] += 1
        key = tuple(freq) 
        # here we grouping the strings
        if key not in anagram_map:
            anagram_map[key]=[]    # here we create a empty list for gouping and it's key is that tuple and value is now empty list
        anagram_map[key].append(word)
    return list(anagram_map.values())    # here we create a list of the values of the hashTable
    
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))