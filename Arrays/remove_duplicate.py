# def remove_duplicate():
#     nums=[1,1,1,2,2,3,3,4]
#     index = 0
#     for i in range(1,len(nums)):       
#         if nums[index] != nums[i]:      
#             index = index+1            
#             nums[index] = nums[i]          
#     return index+1
# print(remove_duplicate())




def remove_duplicate():
    nums=[1,1,1,2,2,3,3,4] 
    index = 0
    for i in range(1,len(nums)):       
        if nums[index] != nums[i]:      
            index = index+1             
            nums[index] = nums[i]      
    for i in range(index+1):
        print(nums[i])
remove_duplicate()      