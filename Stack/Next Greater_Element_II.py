# def next_greater_element(nums):
#     n = len(nums)
#     answer = []
#     stack = []
#     answer = [0]*n
#     for i in range(2*n): 
#         real_index = i%n
#         while stack and nums[real_index]>nums[stack[-1]]:
#             top_index = stack.pop()
#             answer[top_index]= nums[real_index]    
#         if i<n:
#             stack.append(i)
#     while stack and answer[stack[-1]] == 0 :
#         answer[stack[-1]] = -1        
#         stack.pop()
#     return answer
# print(next_greater_element([5,4,3,2,1]))    

def next_greater_element(nums):
    n = len(nums)
    answer = []
    stack = []
    answer = [-1]*n
    for i in range(2*n): 
        real_index = i%n
        while stack and nums[real_index]>nums[stack[-1]]:
            top_index = stack.pop()
            answer[top_index]= nums[real_index]    
        if i<n:
            stack.append(real_index)
    return answer
print(next_greater_element([1,2,1]))    