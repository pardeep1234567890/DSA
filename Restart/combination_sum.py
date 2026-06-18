# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

# Example 1:

# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
# Example 2:

# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

def all_unique_combinations(self, candidates, target):
    result = [] # we define this for storing the result in the list 
    current_candidates = [] # we initialize this to add every combination 
    # for backtrack we define the function to check the every combination
    def backtrack(index,target):   # here candidate is the current number from the array that we will compare to the current number 
        # here we define the base case 
        if index == len(candidates):
            return 
        if target<0:
            return 
        if target == 0 :
            result.append(current_candidates[:])
            return 
        current_candidates.append(candidates[index])
        backtrack(index, target - candidates[index])
        current_candidates.pop()
        backtrack(index+1,target)

    backtrack(0,target) 
    return result 


#  In line number 22 the index parameter helps us to prevent to use duplicate because (index+1) we will move to the next value and never use previous values 
# we use pop to check the every possible combination 

# we start the backtrack to make the every possible combination
# then we define the base cases : (we define the base case related to every given thing)
#    if the target is less than 0 then return 
#    if the target is equal to 0 
