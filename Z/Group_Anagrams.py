def group_anagrams(strs):
    anagram_hash = {}
    for word in strs:
        freq = [0]*26
        for char in word:
            freq[ord(char)-ord("a")] += 1
        key = tuple(freq)
        if key not in anagram_hash: 
            anagram_hash[key] = []
        anagram_hash[key].append(word)
    return list(anagram_hash.values())    

# The time complexity will be O(N*K) because I was thinking like O(n^2) but it is not n^2. It will be O(N*K) because K will be the max length of the string. 