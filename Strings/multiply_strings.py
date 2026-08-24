# 43. Multiply Strings
# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
# Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

# Example 1:

# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:

# Input: num1 = "123", num2 = "456"
# Output: "56088"

def mul_strings(num1,num2):
    if num1 == "0" or num2 == "0":
        return "0"
    res = [0]* (len(num1)+len(num2))
    for i in range(len(num1)-1,-1,-1):
        num1_val = ord(num1[i]) - ord("0")
        for j in range(len(num2)-1,-1,-1):
            num2_val = ord(num2[j])- ord("0")
            mul = num1_val * num2_val
            total = mul + res[i+j+1]
            res[i+j+1]= total%10
            res[i+j] += total//10
    for i in range(len(res)):
        res[i] = str(res[i])
    res_string = "".join(res)
    return res_string.lstrip("0")

print(mul_strings("2","3"))


class Solution:
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"

        result = str(int(num1) * int(num2))
        return result