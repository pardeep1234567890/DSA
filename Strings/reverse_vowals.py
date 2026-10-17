# 345. Reverse Vowels of a Stringto 
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

# Example 1:
# Input: s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

def reverse_vowals(s):
    hash_set = {'a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O','U'}
    left = 0
    right = len(s)-1
    list_s = list(s)
    while left < right :
        if list_s[left] in hash_set and list_s[right] in hash_set:
            list_s[left] ,list_s[right] = list_s[right],list_s[left]
            left += 1
            right -=1
        elif list_s[left] not in hash_set:
            left += 1
        else :
            right -= 1
    return "".join(list_s)
print(reverse_vowals("IceCreAm"))