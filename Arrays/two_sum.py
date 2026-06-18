# This is the brute force solution 
# def twoSum():
#     nums = [1, 2, 3, 4, 5]
#     target = 8
#     n = len(nums)
#     for i in range(n):
#         # Start j from i+1 to avoid using the same element twice and duplicate pairs
#         for j in range(i + 1, n):
#             if (nums[i] + nums[j]) == target:
#                 print(f"Indices: {i}, {j} | Values: {nums[i]}, {nums[j]}")
#                 return 
#     print("nothing")

# twoSum()



# This is the optimized solution 

def twosum():
    nums = [1,2, 3, 4, 5]
    mp = {}
    target = 8
    for i,item in enumerate(nums):
       complement = target-item
       if complement in mp:
           return mp[complement],i
       mp[item] = i
print(twosum())
