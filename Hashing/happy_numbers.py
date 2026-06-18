def is_happy(n):
    def get_sum_of_squares(num):
        total = 0
        while num > 0:
            digit = num%10
            total = total + (digit * digit)
            num = num//10
        return total 
    my_set = set()
    while n != 1 and n not in my_set:
        my_set.add(n)
        n = get_sum_of_squares(n)
    if n in my_set:
        return False
    elif n ==1:
        return True         
print(is_happy(19))


# def is_happy(n):
#     def get_sum_of_squares(num):
#         sum = 0
#         while num > 0:
#             digit = num%10
#             sum = sum + (digit * digit)
#             num = num//10
#         return sum 
#     my_set = set()
#     while n != 1 and n not in my_set:
#         my_set.add(n)
#         n = get_sum_of_squares(n)
#     return n ==1       
# print(is_happy(19))