# def sort_color(nums):
#     left = 0
#     right = len(nums)-1
#     while left < right:
#         if nums[left]> nums[right]:
#             nums[left],nums[right] = nums[right],nums[left]
#             right -=1
#         else:
#             if nums[left] == 0:
#                 left +=1
#     return nums
# print(sort_color([1,0,2]))

# def sort_color(nums):
#     left = 0
#     mid = 0
#     right = len(nums)-1
#     while mid <= right:
#         if nums[mid]== 0:
#             nums[left],nums[mid] = nums[mid],nums[left]
#             left +=1
#             mid +=1
#         elif nums[mid]==2:
#             nums[right],nums[mid] = nums[mid],nums[right]
#             right -=1
#         else:
#             mid +=1
#     return nums
# print(sort_color([1,0,2]))

def sort_color(nums):
    hash_sort = {}
    for i in range(len(nums)):
        hash_sort[nums[i]] = hash_sort.get(nums[i],0)+1
    index = 0
    
    for color in [0,1,2]:
        count = hash_sort.get(color,0)
        for _ in range(count):
            nums[index] = color 
            index += 1 
    return nums
print(sort_color([1,0,2]))