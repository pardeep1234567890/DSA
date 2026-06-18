# Given two strings s and t, return the minimum window substring
# of s such that every character in t (including duplicates) is
# included in the window. If there is no such window, return "".

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"


# first i will hashing the t string
# then i will traverse the s string and check that s string char is in the hash or not ?
# if it is in the hash then i will remove that char from hash if it's freq become 0 and move the right char 
# but i am confuse when to move left pointer 

# Move right until the need couter become zero 
# shrink when the need counter become zero after that shrink the window till the counter remains 0 
# update the answer when we will get the window

def min_window(s,t):
    hash_map_t = {}
    for char in t :
        hash_map_t[char] = hash_map_t.get(char,0)+1
    left = 0
    need = len(t)
    best_len = float('inf')
    for right in range(len(s)):
        if s[right] in hash_map_t:
            if hash_map_t[s[right]] >0 :
                need -= 1 
            hash_map_t[s[right]] = hash_map_t.get(s[right],0)-1
        while need == 0:
            if right-left+1 < best_len:
                best_left, best_len = left, right - left + 1
            if s[left] in hash_map_t:
                hash_map_t[s[left]] = hash_map_t.get(s[left],0)+1
                if hash_map_t[s[left]] >0 :
                    need += 1    
            left +=1
    if best_len == float("inf"):
        return ""
    else:
        return s[best_left:best_left+best_len]