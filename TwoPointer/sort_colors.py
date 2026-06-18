# def sort_colors(nums):
#     index = 0 # this will going to track the same element
#     # current_num = 0 
#     n= len(nums)-1
#     for i in range(len(nums)):
#         if nums[i] == 0 and i<n:
#             nums[index] , nums[i] = nums[i] ,nums[index]
#             index +=1
#         elif nums[i] == 2 and i<n:
#             nums[n] ,nums[i]= nums[i],nums[n]
#             n -= 1
#         else:
#             continue
#     print(nums)        
# print(sort_colors([2,0,0,1,2]))


# def sort_colors(nums):
#     index = 0 # this will going to track the same element
#     # current_num = 0 
#     n= len(nums)-1
#     for i in range(len(nums)):
#         index = i
#         while nums[index] == 0 and index<n:
#             nums[0] , nums[i] = nums[i] ,nums[0]
#             index +=1

#         while nums[index] == 2 and index<n:
#             nums[n] ,nums[i]= nums[i],nums[n]
#             index +=1
#     print(nums)        
# print(sort_colors([2,0,2,1,1,0]))


# def sort_colors(nums):
#     index = 0 # this will going to track the same element
#     # current_num = 0 
#     n= len(nums)-1
#     for i in range(len(nums)):
#         while nums[i] == 0 and index <:
#             nums[index] , nums[i] = nums[i] ,nums[index]
#             index +=1
#         while nums[i] == 2 and i<n:
#             nums[n] ,nums[i]= nums[i],nums[n]
#             n -= 1
#     return nums        
# print(sort_colors([2,0,2,1,1,0]))

# def sort_colors(nums):
#     low = 0 # this will going to track the same element
#     mid= 0 
#     high = len(nums)-1
#     while mid<=high:
#         if nums[mid] == 1 :
#             mid +=1
#         elif nums[mid] == 0:
#             nums[low] ,nums[mid]= nums[mid],nums[low] 
#             low +=1
#             mid +=1
#         else:
#             nums[high],nums[mid]= nums[mid],nums[high]  
#             high -=1     
#     return nums
# print(sort_colors([2, 2, 0, 1, 1, 0]))


def sortColors(nums):
        left = 0      
        right = len(nums) - 1  
        current = 0   
        while current <= right:
            if nums[current] == 0:
                nums[left], nums[current] = nums[current], nums[left]
                left += 1
                current += 1
            elif nums[current] == 2:
                nums[right], nums[current] = nums[current], nums[right]
                right -= 1
            else:  
                current += 1
        return nums        
print(sortColors([2, 2, 0, 1, 1, 0]))

# nums[left] , we know it's either 0,1 because the nums[current] will ahead or on the same position with nums[left] and if nums[current] is 2 then it already processed and another condition nums[current] is 0 or 1 then nums[left] only lefts 0 or 1 on the left side   

# nums[left], we know it's either 0 or 1 because nums[current] will be ahead or on the same position with nums[left]
# ✅ Correct! current >= left always.

# Why NOT a 2 at nums[left]?
# Because if we ever saw a 2 at current, we swapped it to the right side and didn't move current forward. So 2s never get left behind between left and current.
