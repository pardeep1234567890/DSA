# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321

def reverse_integer(x):
    result = 0
    sign = -1 if x<0 else 1
    x = abs(x)
    while x:
        value = x %10 
        if not -2**31<result*10 + value<2**31:
            return 0
        result = result*10 + value
        x = x//10 
    return result*sign

print(reverse_integer(-12345678))
 
#  if  result > (2**31-value)//10:
#             return 0