# 40. Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# so the difference in between combination 1 and combination 2 is that in this problem we can't use same index number again ?
# def combination_sum_II(candidates,target):
#     candidates.sort()
#     result = []
#     def backtrack(index,target,path):
#         if target == 0:
#             result.append(path[:])
#             return 
#         if index == len(candidates):
#             return 
#         if target < 0 :
#             return
#         i = index 
#         while i<len(candidates) and candidates[i] == candidates[index]:
#             i += 1
#         backtrack(i,target,path)
#         path.append(candidates[index])
#         backtrack(index+1,target-candidates[index],path)
#         path.pop()
#     backtrack(0,target,[])
#     return result
        
    
class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()          # Sort to handle duplicates easily
        result = []
        
        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])   # Found a valid combination
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):  # here we use start because of not using the same number again 
                
                # Early pruning
                if candidates[i] > remaining:
                    break
                 # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i], path)  # i+1 → each number used at most once
                path.pop()
        
        backtrack(0, target, [])
        return result

    


