# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# def first_last_position(nums,target): 
#     def find_first(left,right):
#         result = -1
#         while left <= right:
#             mid = (left+right) //2
#             if nums[mid] == target :
#                 right = mid -1
#                 result = mid 
#             elif nums[mid] < target:
#                 left = mid +1
#             else : 
#                 right = mid-1
#         return result
#     def find_last(left,right):
#         result = -1
#         while left <= right:
#             mid = (left+right) //2
#             if nums[mid] == target :
#                 left = mid +1 
#                 result = mid 
#             elif nums[mid] < target:
#                 left = mid +1
#             else : 
#                 right = mid-1
#         return result  
#     final_result = [find_first(0,len(nums)-1),find_last(0,len(nums)-1)]
#     return final_result


def first_last_position(nums,target): 
    def find_first(left,right,find_first_flag):
        result = -1
        while left <= right:
            mid = (left+right) //2
            if nums[mid] == target :
                result = mid
                if find_first_flag:
                    right = mid -1
                else : 
                    left = mid+1
            elif nums[mid] < target:
                left = mid +1
            else : 
                right = mid-1
        return result
    final_result = [find_first(0,len(nums)-1,True),find_first(0,len(nums)-1,False)]
    return final_result