# def top_elements(nums,k):
#     nums_dict ={}
#     most_frequent_value = 0
#     most_frequent_number = 0
#     nums_list = []
#     for num in nums:
#         nums_dict[num] = nums_dict.get(num,0)+1
#     for num in (nums_dict):                   
#         if nums_dict[num] > most_frequent_value:
#             most_frequent_value = nums_dict[num]
#             most_frequent_number = num
#             nums_list.append(most_frequent_number) 
#         del nums_dict[num]            
#     return nums_list    
    
# print(top_elements([1,1,1,2,2,3],2))    


#  this is the Unoptimized approach 
# def top_elements(nums,k):
#     nums_dict ={} 
#     most_frequent_value = 0
#     most_frequent_number = 0
#     nums_list = []
#     for num in nums:
#         nums_dict[num] = nums_dict.get(num,0)+1
#     while k>0:  
#         most_frequent_value = 0
#         most_frequent_number = 0
#         for num in (nums_dict):                 
#             if nums_dict[num] > most_frequent_value:
#                 most_frequent_value = nums_dict[num]
#                 most_frequent_number = num

#         nums_list.append(most_frequent_number) 
#         del nums_dict[most_frequent_number]    
#         k -=1        
#     return nums_list    
    
# print(top_elements([1], 1))   


# def top_elements(nums,k):
#     nums_dict ={}
#     top_elements_list = []
#     for num in nums:
#         nums_dict[num] = nums_dict.get(num,0)+1
#     dict_items = nums_dict.items()                   # this is the way to get the key value pairs
#     sorted_list = sorted(dict_items,key = lambda item: item[1]  ,reverse=True)
#     while k>0:
#         element = sorted_list[0][0]
#         top_elements_list.append(element)
#         sorted_list.pop(0)
#         k-=1

#     return top_elements_list    
# print(top_elements([1,1,1,2,2,3],2))

def top_elements(nums,k):
    nums_dict ={}
    top_elements_list = []
    for num in nums:
        nums_dict[num] = nums_dict.get(num,0)+1
    dict_items = nums_dict.items()                   # this is the way to get the key value pairs
    sorted_list = sorted(dict_items,key = lambda item: item[1]  ,reverse=True)
    top_k = sorted_list[:k]
    for item in top_k:
        element = item[0]
        top_elements_list.append(element)

    return top_elements_list    
print(top_elements([1,1,1,2,2,3],2))