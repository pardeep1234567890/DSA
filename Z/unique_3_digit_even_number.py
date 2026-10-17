# 3483. Unique 3-Digit Even Numbers
# You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.
# Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

# def Total_even_numbers(digits):
#     hash_map = {}
#     counter = 0
#     for digit in digits:
#         hash_map[digit] = hash_map.get(digit,0)+1
#     for i in range(100,1000,2):
#         hash_map_2 = {}
#         valid = True
#         string = str(i)
#         new_arr = list(string)
#         for digit in new_arr:
#             hash_map_2[int(digit)] = hash_map_2.get(int(digit),0)+1
#         for digit , count in hash_map_2.items():
#             if digit not in  hash_map or count> hash_map[digit]:
#                 valid = False
#                 break
#         if valid:
#             counter +=1
#     return counter

# print(Total_even_numbers([1,2,3,4]))

def numbers(digits):
    num_set = set()
    for i in range(len(digits)):
        for j in range(len(digits)):
            for k in range(len(digits)):
                if i == j or j ==k or i ==k :  # each copy of digit can only be used once
                    continue
                if digits[i] != 0 and digits[k] %2 == 0:
                    number = digits[i]*100 + digits[j] * 10 + digits[k] 
                    num_set.add(number)
    return len(num_set)
print(numbers([1,2,3,4]))