# You're given strings jewels representing the types of stones that are jewels, and stones representing 
# the stones you have. Each character in stones is a type of stone you have. 
# You want to know how many of the stones you have are also jewels.
# Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Example 1:

# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3

def numJewelsInStones(jewels, stones):
    hash_map = {}
    result = 0
    for char in stones:
        hash_map[char]= hash_map.get(char,0)+1 
    for char in jewels:
        if char in hash_map:
            result += hash_map[char]
    return result

print(numJewelsInStones("z", "ZZ"))