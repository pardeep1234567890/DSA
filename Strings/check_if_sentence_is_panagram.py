# 1832. Check if the Sentence Is Pangram
# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
 

# Example 1:

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:

# Input: sentence = "leetcode"
# Output: false


def check_str(s):
    if len(s) < 26 :
        return False
    new_set = set()
    for char in s:
        new_set.add(char)
        if len(new_set) == 26:
            return True
    return False 

print(check_str("thequickbrownfoxjumpsoverthelazydog"))