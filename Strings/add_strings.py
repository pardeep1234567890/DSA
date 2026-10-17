# 415. Add Strings
# Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
# You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.


# Example 1:
# Input: num1 = "11", num2 = "123"
# Output: "134"


# def add_strings(num1 , num2):
#     p1 = len(num1)-1
#     p2 = len(num2)-1
#     carry = 0
#     result = ""
#     while p1>=0 or p2 >=0 or carry != 0:
#         if p1>=0 :
#             dig1 = num1[p1]
#         else :
#             dig1 =0
#         if p2>=0 :
#             dig2 = num2[p2]
#         else :
#             dig2=0
#         total = int(dig1) + int(dig2) + carry
#         p1 -= 1
#         p2 -= 1
#         result += str(total%10)
#         carry = total//10
#     return result[::-1]



# print(add_strings("456","77"))

def add_strings(num1 , num2):
    p1 = len(num1)-1
    p2 = len(num2)-1
    carry = 0
    result = []
    while p1>=0 or p2 >=0 or carry != 0:
        if p1>=0 :
            dig1 = ord(num1[p1]) - ord("0")
        else :
            dig1 =0
        if p2>=0 :
            dig2 = ord(num2[p2]) - ord("0")
        else :
            dig2=0
        total = int(dig1) + int(dig2) + carry
        p1 -= 1
        p2 -= 1
        result.append(str(total%10))
        carry = total//10
    new_res= "".join(result)
    return new_res[::-1]

print(add_strings("11","123"))
