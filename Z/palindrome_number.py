# 9. Palindrome Number
# Given an integer x, return true if x is a palindrome, and false otherwise.
# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

def pal_num(x):
    if x < 0 :
        return False
    number = x
    result = 0 
    while  number:
        num = number% 10 
        result = result*10+num 
        number = number // 10 
    if result == x :
        return True
    else : 
        return False
    

# i was trying to solve this problem using string strategy but i should solve it using mathematical way
# we can also solve this problem using string , like reverse the string and then can compare them  