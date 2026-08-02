# 451. Sort Characters By Frequency
# Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.
# Return the sorted string. If there are multiple answers, return any of them.


# Example 1:

# Input: s = "tree"
# Output: "eert"
# Explanation: 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

def frequency_sort(s):
    hash_map = {}
    result = ""
    for char in s :
        hash_map[char] = hash_map.get(char,0)+1
    new_list = sorted(hash_map,key = lambda x:hash_map[x],reverse=True)

    for char in new_list:
        result += char * hash_map[char]
    return result
print(frequency_sort("Aabb"))