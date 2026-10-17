# 38. Count and Say
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Run-length encoding (RLE) is a string compression method that works by replacing each maximal group of consecutive identical characters with the concatenation of the length of the group followed by the character itself. For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15", and replace "1" with "11". Thus the compressed string becomes "23321511".
# Given a positive integer n, return the nth element of the count-and-say sequence.

# Example 1:
# Input: n = 4
# Output: "1211"

# Explanation:
# countAndSay(1) = "1"
# countAndSay(2) = RLE of "1" = "11"
# countAndSay(3) = RLE of "11" = "21"
# countAndSay(4) = RLE of "21" = "1211"

def count_and_say(n):
    if n == 1 :
        return "1"
    string = count_and_say(n-1)
    curr_char = string[0]
    count = 1
    result = ""
    for i in range(1,len(string)): 
        if curr_char == string[i]:
            count += 1
        else:
            result += str(count) + curr_char 
            curr_char = string[i]
            count = 1
    result += str(count) + curr_char # this is for the last group 
    return result