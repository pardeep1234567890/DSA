# 67. Add Binary
# Given two binary strings a and b, return their sum as a binary string.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"

def add_binary(a,b):
    if len(a) > len(b):
        b = "0" * (len(a)-len(b)) + b 
    else:
        a = "0" * (len(b) - len(a)) + a

    carry = 0 
    result = ""
    for i in range(len(a)-1,-1,-1):
        total = int(a[i])+int(b[i])+carry
        digit = total%2
        carry = total//2
        result = str(digit) + result 
    if carry == 1 :
        result = str(carry) + result
    return result

print(add_binary("11","1"))



# --------------------------------------------------
# def addBinary(a, b):
#         a=int(a,2)
#         b=int(b,2)
#         c=bin(a+b)
#         return c.replace("0b","")
        