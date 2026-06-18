def string_to_integer(s):
    integer = 0
    INT_MIN = -2147483648
    INT_MAX =  2147483647
    sign = 1
    i = 0 
    n = len(s)
    while i<n and s[i] == " ":
        i+=1
    if i<n and s[i] == "-":
        sign = -sign  
        i+=1
    elif i<n and s[i] == "+":
        i+=1  

    if i<n and not "0" <= s[i] <= "9":
        return 0          
    while i<n and s[i].isdigit():
        integer= integer*10+int(s[i])
        i = i+1                
    integer = sign * integer
    if integer < INT_MIN:
        return INT_MIN        
    elif integer > INT_MAX:
        return INT_MAX
    else:
        return integer    

print(string_to_integer("   42"))