# Given a string s, return true if the string can be a palindrome
# after deleting at most one character.

# Example 1:
# Input: s = "abca"
# Output: true

# we have to delete only if necessary 
# first we try without deleting 
# how to find which character we should delete 

# one pointer at start and one pointer at last
# Then i will move the pointer inside if they are equal and if they don't equal then thought to remove the character (which side character left/right?) can delete any side character 
# then check that they are similar or not ? if i have to remove once then i will define it outside the loop 

def valid_palindrome_II(s):
    left = 0
    right = len(s)-1
    while left<right:
        if s[left] == s[right]:
            left +=1
            right -=1
        else:
            slice_without_left = s[left+1:right+1]
            slice_without_right = s[left:right]
            if slice_without_left == slice_without_left[::-1] or slice_without_right == slice_without_right[::-1]:
                return True
            else: 
                return False
    return True
print(valid_palindrome_II("abc"))