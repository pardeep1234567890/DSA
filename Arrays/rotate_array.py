# this is the three step solution problem 
# reverse teh entire array
# reverse first k elements 
# reverse the remaining n-k elements

# def rotate_array(k):
#     nums = [1,2,3,4,5,6,7]
#     n = len(nums)-1
#     end = k-1
#     last = len(nums)-1
#     for i in range(len(nums)):
#         if i<n :
#             temp = nums[i]
#             nums[i] = nums[n]
#             nums[n] = temp
#             n = n-1
#             # i = i+1
#     for i in range(k):
#         if i < end:
#             temp = nums[i]
#             nums[i] = nums[end]
#             nums[end] = temp
#             # i =i+1
#             end = end-1
#     for i in range(k,len(nums)):
#         if i< last:
#             temp = nums[i]
#             nums[i] = nums[last]
#             nums[last] = temp
#             # i = i+1
#             last= last-1
#     return nums


# print(rotate_array(8))


# def rotate_array(nums,k):
#     k = k%len(nums)
#     right_ptr = len(nums)-1
#     end = k-1
#     end_ptr = len(nums)-1
#     for i in range(len(nums)):
#         if i<right_ptr :
#             temp = nums[i]
#             nums[i] = nums[right_ptr]
#             nums[right_ptr] = temp
#             right_ptr = right_ptr-1
#     for i in range(k):
#         if i < end:
#             temp = nums[i]
#             nums[i] = nums[end]
#             nums[end] = temp
#             end = end-1
#     for i in range(k,len(nums)):
#         if i< end_ptr:
#             temp = nums[i]
#             nums[i] = nums[end_ptr]
#             nums[end_ptr] = temp
#             end_ptr= end_ptr-1
#     return nums
# print(rotate_array([1,2,3,4,5,6,7],8))


# def reverse(start,end)
# def rotate_array(nums,k):
#     if not nums:
#         return nums
#     k = k%len(nums)
#     right_ptr = len(nums)-1
#     end = k-1
#     end_ptr = len(nums)-1
#     for i in range(len(nums)):
#         if i<right_ptr :
#             nums[i] , nums[right_ptr] = nums[right_ptr],nums[i] # here we exchange the values without using temp variable
#             right_ptr = right_ptr-1
#     for i in range(k):
#         if i < end:
#             nums[i],nums[end] = nums[end],nums[i]
#             end = end-1
#     for i in range(k,len(nums)):
#         if i< end_ptr:
#             nums[i],nums[end_ptr] = nums[end_ptr],nums[i]
#             end_ptr= end_ptr-1
#     return nums
# print(rotate_array([1,2,3,4,5,6,7],3))


def rotate_array(nums,k):
    # these are the edge cases like if nums array is empty or k(it is a positive integer that tells how much times to rotate array) is greater than the length of array
    if not nums:
        return nums
    k = k%len(nums)
    # here we define a function for reverse array b/z we need to reverse array here 3 times
    def reverse_array(left,right):
        while left<right:
            nums[left],nums[right] = nums[right],nums[left]
            left += 1
            right -= 1 

    # now we here reverse the array 
    # 1. reverse the entire array
    reverse_array(0,len(nums)-1)
    # 2. rotate till k 
    reverse_array(0,k-1)
    # 3. rotate n-k left elements
    reverse_array(k,len(nums)-1)
    return nums

print(rotate_array([1,2,3,4,5,6,7],3))