# def trapping_rain_water():
#     nums = [0,1,0,2,1,0,1,3,2,1,2,1]
#     n = len(nums)
#     right_max_array = [0]*n
#     right_max = nums[n-1]
#     right_max_array[n-1] = right_max
#     left_max_array = []
#     left_max = nums[0]
#     left_max_array.append(left_max)
#     total_water = 0
#     for i in range(1,len(nums)):
#         if nums[i]>left_max:
#             left_max = nums[i]
#             left_max_array.append(nums[i])
#         else:
#             left_max_array.append(left_max)
#     for i in range(len(nums)-2,-1,-1):
#         if  nums[i]>right_max:
#             right_max= nums[i]
#             right_max_array[i] = nums[i] # here we use 0 to prepand at the begining 
#         else:
#             right_max_array[i] = right_max  
#     for i in range(len(nums)):
#         trapped_water = min(left_max_array[i],right_max_array[i])-nums[i] 
#         total_water = trapped_water + total_water          
#     return total_water
# print(trapping_rain_water())


# i have to use two pointer technique only , i did mistake here that i mixed optimized and brute force technique both
def trapping_rain_water():
    nums = [4,2,0,3,2,5]
    left = 0
    right = len(nums)-1
    left_max = 0
    right_max = 0 
    total_water = 0
    while left<right:
        if nums[left] < nums[right]:
            if nums[left] >= left_max:
                left_max= nums[left]
            total_water += left_max - nums[left]     
            left += 1
        else:
            if nums[right] >= right_max:
                right_max = nums[right]
            total_water += right_max - nums[right]    
            right -=1  
    return total_water
print(trapping_rain_water())