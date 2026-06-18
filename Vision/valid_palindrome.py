# i will convert the uppercase letters into lowercase then check of the character is alphanumeric or not if not alphanumric then skip 
# else compare the char and  move the pointer and return true if all the char matches

def valid_palindrome(s):
    new_string = s.lower()  # a man, a plan, a canal: panama
    left = 0
    right = len(s)-1
    while left < right:
        if not new_string[left].isalnum():
            left +=1 
        elif not new_string[right].isalnum():
            right -=1
        else:
            if new_string[left] == new_string[right]:
                left +=1 
                right -=1
            else:
                return False
    return True 
print(valid_palindrome("A man, a plan, a canal: Panama"))