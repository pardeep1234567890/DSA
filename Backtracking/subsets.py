# Now I will go to defining the helper function for the backtracking in the subset problem. 
# I will define the base case, like we usually do in recursion. Then I will define the two choices that we will make, 
# like whether to include or not the current number and 
# make a recursive function to do the same thing till end (called Helper function)

def subsets(nums):
    current_subset = []
    result = []
    def backtrack(index):
        # This is the base case 
        if index == len(nums):
            result.append(current_subset[:]) #we append a copy
            return  # --> This line exactly return it just after the backtrack() called inside the function means just after where it leavesevery time
        # 1. Now i will define the include branch 
        current_subset.append(nums[index])  # 1. here we make the choice basically include
        backtrack(index+1)  # 2. Explore that choice (move to next level)
                        
        current_subset.pop()                # 3. Undo the choice (backtrack!)
        
        # 2. Now i will define the Exclude choice 
        backtrack(index+1)

    backtrack(0)
    return result 
print(subsets([1,2]))