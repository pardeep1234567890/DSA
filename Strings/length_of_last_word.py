# 58. Length of Last Word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

# def len_last_word(s):
#     print(s.strip(" "))
#     new_string = s[-1]
#     # print(new_string)
#     return len(new_string)

# print(len_last_word("fly me   to    the moon   "))


def len_last_word(s):
    new_string = s.strip()
    array = new_string.split(" ")
    last_word = array[-1]
    return len(last_word)

print(len_last_word("fly me to the moon"))