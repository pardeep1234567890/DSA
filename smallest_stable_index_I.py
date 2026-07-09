# def firstStableIndex( nums, k):
#     n = len(nums)
#     max_num = float("-inf")
#     min_num = float("inf")
#     ans = [0]*n
#     for i in range(n):
#         for j in range(i+1):
#             if max_num < nums[j]:
#                 max_num = nums[j]
#             # max_num = max(max_num,nums[j])
#         for l in range(i,n):
#             if min_num>nums[l]:
#                 min_num = nums[l] 
#             # min_num = min(min_num,nums[l])
#         ans[i] = max_num-min_num
#         max_num = float("-inf")
#         min_num = float("inf")
#         if ans[i]<=k:
#             return i
#     return -1        
# print(firstStableIndex( [0],  0))


# Optimized Approach = prefix_max, suffix_min 

def firstStableIndex( nums, k):
    n = len(nums)
    max_num = float("-inf")
    min_num = float("inf")
    ans = [0]*n
    for l in range(n-1,-1,-1):
            if min_num>nums[l]:
                min_num = nums[l]
                ans[l] = min_num
            else :
                ans[l]= min_num    
    for i in range(n):
        if max_num < nums[i]:
            max_num = nums[i]
        ans[i] = max_num-ans[i]
        if ans[i]<=k:
            return i
    return -1        
print(firstStableIndex( [0],  0))
