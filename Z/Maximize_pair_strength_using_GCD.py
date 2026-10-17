# Q1. Maximize Pair Strength Using GCD
# You are given an integer array nums.
# Choose exactly one pair of distinct indices i and j. The strength of the pair is defined as (nums[i] * nums[j]) / gcd(nums[i], nums[j])2.
# Return the maximum strength over all possible pairs.
# The term gcd(a, b) denotes the greatest common divisor of a and b.

def maxPairStrength(nums):
    def gcd(a,b):
        if b == 0:
            return a 
        return gcd(b,a%b)
    sorted_nums = sorted(nums, reverse=True)
    best = 0
    for i in range(len(sorted_nums)-1):
        if sorted_nums[i]* sorted_nums[i+1] <= best:
            break
        for j in range(i+1, len(sorted_nums)-1):
            if sorted_nums[i] * sorted_nums[j] <= best :
                break
            g = gcd(sorted_nums[i],sorted_nums[j])
            strength = (sorted_nums[i]* sorted_nums[j])/(g*g)
            best = max(best,strength)
    return best 