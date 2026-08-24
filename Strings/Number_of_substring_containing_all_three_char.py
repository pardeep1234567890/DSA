# 1358. Number of Substrings Containing All Three Characters
# Given a string s consisting only of characters a, b and c.
# Return the number of substrings containing at least one occurrence of all these characters a, b and c.
 

# Example 1:
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
# Example 2:

# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
# Example 3:

# Input: s = "abc"
# Output: 1

def num_substring_containing_all_char(s):
    count_a , count_b , count_c = 0,0,0
    left = 0
    subarr_count = 0
    n = len(s)
    for right in range(len(s)):
        if s[right] == "a":
            count_a += 1
        elif s[right] == "b":
            count_b += 1
        else :
            count_c += 1
        while count_a >= 1 and count_b >=1 and count_c >=1:
            subarr_count += n-right
            if s[left] == "a":
                count_a -= 1
            elif s[left] == "b":
                count_b -= 1
            else :
                count_c -= 1
            left +=1
    return subarr_count
print(num_substring_containing_all_char("abc"))

        


