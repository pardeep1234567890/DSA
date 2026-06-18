# i did the mistake that i am stroing the data in the string but i should do it in the list 
# def reverse_words(s):
#     l = []
#     l = s.split()
#     s1 = ""
#     for i in range(len(l)-1,-1,-1):
#        s1  = s1+l[i]    
           
#     return  "".join(s1)
# print(reverse_words("  hello welcome  "))    

# def reverse_words(s):
#     list_s = s.split()
#     list_reverseWords =[]
#     for i in range(len(list_s)-1,-1,-1):
#         list_reverseWords.append(list_s[i]) 
#     return  " ".join(list_reverseWords)
# print(reverse_words("welcome   to the world   of pardeep    ")) 


# def reverse_words(s):
#     l = s.split()
#     # l.reverse()
#     # return " ".join(l)
# print(reverse_words("Hello  world ")) 


def reverse_words(s):
    list_s = s.split()
    l2 = list_s[::-1]
    return " ".join(l2)
print(reverse_words("welcome   to the world   of pardeep    "))