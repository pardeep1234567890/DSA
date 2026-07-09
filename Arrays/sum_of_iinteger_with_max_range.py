# class Solution(object):
#     def maxDigitRange(self, nums):
#         max_range = -1
#         total_sum = 0
#         for num in nums:
#             s = str(num)
#             largest_char = max(s)
#             smallest_char = min(s)
#             current_range = int(largest_char)-int(smallest_char)

#             if current_range >max_range:
#                 max_range = current_range
#                 total_sum = num
#             else:
#                 if current_range == max_range:
#                     total_sum += num
#         return total_sum

class Solution(object):
    def maxDigitRange(self, nums):
        max_range = -1
        total_sum = 0
        for num in nums:   
            largest_digit = float("-inf")
            smallest_digit = float("+inf")
            temp_num = num
            while temp_num :
                curr_num = temp_num %10
                if largest_digit < curr_num:
                    largest_digit = curr_num
                if smallest_digit > curr_num:
                    smallest_digit = curr_num
                temp_num = temp_num // 10
            current_range = largest_digit - smallest_digit
            if num == 0 :
                current_range = 0 
            if current_range > max_range :
                max_range = current_range
                total_sum = num 
            else:
                if current_range == max_range:
                    total_sum += num                
            
        return total_sum