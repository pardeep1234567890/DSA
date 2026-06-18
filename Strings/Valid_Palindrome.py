def valid_palindrome(s):
    s1 = s.lower() 
    left = 0
    right = len(s1)-1
    while left < right:
        if not s1[left].isalnum():      # here i didn't know that how to check the alphanumeric character 
            left +=1
        elif not s1[right].isalnum():
            right -=1
        else:
            if s1[left] == s1[right] :
                left += 1
                right -=1
            else: 
                return False    
    return True    

print(valid_palindrome("A man, a plan, a canal: Panama"))