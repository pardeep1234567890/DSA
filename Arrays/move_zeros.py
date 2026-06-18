# This is the two pointer technique 
def move_zeros():
    nums = [0,1,0,3,12]
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0 :
            nums[index] = nums[i]  # here we overwrite 
            if i != index:
                nums[i] = 0
            index += 1
    for item in nums:
        print(item)
move_zeros()                        
            
# def move_zeros():
#     nums = [0,1,0,3,12]
#     index = 0
#     for i in range(len(nums)):
#         if nums[i] != 0 :
#             temp = nums[i]
#             nums[i] = nums[index]
#             nums[index] = temp
#             index += 1
#     for item in nums:
#         print(item)
# move_zeros()    