# 557. Reverse Words in a String III
# Given a string s, reverse the order of characters in each word within a sentence while still 
# preserving whitespace and initial word order.

# Example 1:
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"

def reverse_words_III(s):
    split_String = s.split()
    result = []
    for word in split_String:
        new_word = list(word)
        left = 0
        right = len(new_word)-1
        while left<right :
            new_word[left],new_word[right] = new_word[right],new_word[left]
            left += 1
            right -=1 
        result.append("".join(new_word))

    return " ".join(result)
print(reverse_words_III("Mr Ding"))

