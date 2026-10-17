# ## 🎯 Blind Drill — Interview Style

# Before you write any code for each one, I want you to:
# 1. **Ask me any clarifying questions** (like you would in a real interview)
# 2. **State which pattern you'd use and why** — what specific clue in the problem tipped you off

# Ready? Let's go.
# ---

# ### Problem 1

# > You're given an array of integers and a target integer `k`. I want you to find **how many contiguous subarrays** in this array have a sum exactly equal to `k`.
# >
# > For example, given `[1, 1, 1]` and `k = 2`, your answer would be `2` — the subarrays `[1, 1]` starting at index 0 and `[1, 1]` starting at index 1.

# Take your time. What questions do you have for me, and what's your initial thinking on the approach?


def sub_sum_equal_k(nums,k):
    hash_map = {0:1}
    count = 0
    current_sum = 0
    for i in range(len(nums)):
        current_sum = current_sum + nums[i]
        val = current_sum -k 
        if val in hash_map:
            count += hash_map[val] 
        hash_map[current_sum] = hash_map.get(current_sum,0)+1
    return count  
print(sub_sum_equal_k([1,1,1],2))

