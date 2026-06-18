# def combination_sum(candidates,target):
#     current_candidates = []
#     result = []
#     def backtrack(index,target):
#         # here i will define the base case
#         if index == len(candidates):
#             return 
#         if target <0 :
#             # current_candidates.pop()
#             return
#         if target ==0:
#             result.append(current_candidates[:])
#             return 
#         # here we define the include choices 
#         current_candidates.append(candidates[index])
#         # target = target-candidates[index]
#         backtrack(index,target-candidates[index])

#         #backtrack
#         current_candidates.pop()

#         # now here we define the exclude choice 
#         backtrack(index+1,target)

#     backtrack(0,8)
#     return result
# print(combination_sum([2,3,5]))        


def combination_sum(candidates,target):
    current_candidates = []
    result = []
    def backtrack(index,target):
        if index == len(candidates):
            return 
        if target <0 :
            return
        if target ==0:
            result.append(current_candidates[:])
            return 
        current_candidates.append(candidates[index])
        backtrack(index,target-candidates[index])
        current_candidates.pop() 
        backtrack(index+1,target)

    backtrack(0,target)
    return result
print(combination_sum([2,3,5],8))        