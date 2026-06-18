# we have a brute force method for reverse that is we start traversing from last element of the string and add 
# into a new array/list of string but it takes the extra space O(n)
# So we use two pointers technique for the optimal approach
# def reverse_string():
#     s = "hello"
#     str1 = list(s)
#     left = 0
#     right = len(str1)-1
#     while left < right :
#         str1[left],str1[right] = str1[right],str1[left]
#         left +=1
#         right -=1
#     rev_string =  "".join(str1)   
#     return rev_string
# print(reverse_string())

def reverse_string(s):
    chars = list(s)
    left ,right = 0,len(chars)-1
    while left < right :
        chars[left],chars[right] = chars[right],chars[left]
        left +=1
        right -=1   
    return "".join(chars)
print(reverse_string("hello"))

# Mistake :-
# in this problem i did forget to increment and decrement the Left and Right