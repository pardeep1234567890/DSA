# 1903. Largest Odd Number in String
# You are given a string num, representing a large integer. 
# Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
# A substring is a contiguous sequence of characters within a string.


# Example 1:

# Input: num = "52"
# Output: "5"
# Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.

# def largest_odd_number(num):
#     # result = num[0]
#     result = ""
#     for i in range(len(num)):
#         if int(num[i]) 
#     while n :
#         if int(result) %2 != 0:

#         result += num[i]
#         i+=1
#         n-=1
#     max_result = max(max_result,int(result))
#     result = ""
#     return ""        
# print(largest_odd_number("35427"))


def largest_odd_number(num):
    for i in range(len(num)-1,-1,-1):
        if int(num[i])%2 != 0:
            return num[:i+1] 
    return ""
print(largest_odd_number("52"))