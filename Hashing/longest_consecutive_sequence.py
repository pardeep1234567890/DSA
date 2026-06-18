# def longest_consecutive(nums):
#     num_set = set()
#     consecutive_array = []
#     max_len = 0
#     for num in nums:
#         num_set.add(num)    
#     for i in range(len(nums)):
#         if nums[i]-1 not in num_set:
#             consecutive_array.append(nums[i])
#             if nums[i]+1 in num_set:
#                 while nums[i]+1 in num_set:
#                     consecutive_array.append(nums[i]+1)
#                     nums[i] +=1   
#             max_len = max(max_len,len(consecutive_array))
#             consecutive_array = [] 
#     return max_len

# print(longest_consecutive([1,0,2]))    


# def longest_consecutive(nums):
#     num_set = set(nums)
#     counter = 0
#     max_len = 0   
#     for i in range(len(num_set)):
#         if nums[i]-1 not in num_set:
#             current_num = nums[i]
#             counter =1
#             if current_num+1 in num_set:
#                 while current_num+1 in num_set:
#                     counter +=1   
#                     current_num = current_num+1
#             max_len = max(max_len,counter)
#             counter = 0 
#     return max_len

# print(longest_consecutive([1,0,2]))   


def longest_consecutive(nums):
    num_set = set(nums)
    counter = 0
    max_len = 0   
    for num in num_set:
        if num-1 not in num_set:
            current_num = num
            counter =1
            while current_num+1 in num_set:
                counter +=1   
                current_num = current_num+1
            max_len = max(max_len,counter)
    return max_len

print(longest_consecutive([]))   