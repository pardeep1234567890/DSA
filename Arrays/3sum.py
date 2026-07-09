# # Here we basically do 3 main steps
# # 1. Sorting
# # 2. compare using two pointers and fix one element
# # 3. handle duplicates
def three_sum():
    nums = [-1,0,1,2,-1,-4]
    result = []
    # Here i will do sorting
    nums.sort()
    for i in range(len(nums)-2):
        # here we define for skip the dulpicate for i 
        if i >0 and nums[i] == nums[i-1]:
            continue
        L = i+1
        R = len(nums)-1
        while L<R :
            total = nums[i] +nums[L] +nums[R]
            if total<0 :
                L += 1
            elif total>0 :
                R -= 1
            else:
                result.append([nums[i],nums[L],nums[R]]) # to add all the triple elements we should add as list 
                while L<R and nums[L] == nums[L+1]:
                    L +=1
                while L<R and nums[R] == nums[R-1]:
                    R = R-1
                L = L+1
                R = R-1    
    return result            
print(three_sum())


# from collections import defaultdict

# def three_sum_indices(nums):
#     n = len(nums)
#     ans = []

#     for i in range(n - 2):

#         seen = defaultdict(list)

#         for j in range(i + 1, n):

#             target = -(nums[i] + nums[j])

#             if target in seen:
#                 for k in seen[target]:
#                     ans.append([i, k, j])

#             seen[nums[j]].append(j)

#     return ans
# print(three_sum_indices([-1,-1,0,1]))