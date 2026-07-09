# Determine if a given array contains a subarray of at least two elements whose sum is a multiple of a specified number k.
# An array is considered to have a "good subarray" if there exists at least one subarray (consisting of two or more elements) such that the sum of the elements in this subarray is a multiple of k.
# (Note: 0 is considered a multiple of any integer k.)
# For example, the array [23, 2, 4, 7] with k = 6 has a "good subarray" ([2, 4]), as the sum 6 is a multiple of k = 6. The array [5, 0, 0, 0] with k = 3 has a "good subarray", as the subarray [0, 0] sums to 0, which is a multiple of 3.


# i will make the prefix sum array with handling the edge case like if l = 0
# then check if the sum(one index to another index) is equal to multiple of k or not if yes then return true else 
# after completing the array i will return the false and also handle the 0 mulitple case

# now the main problem i thinking in this approach is like how i check all the ranges ?


def check_good_subarray(nums,k):
    prefix = [0]*len(nums)
    for i in range(len(nums)):
        if i ==0 :
            prefix[i] = nums[i]
        else:
            prefix[i] = prefix[i-1]+nums[i]
    print(prefix)

    hash_map = {0:-1}
    for i in range(len(prefix)):
        reminder = prefix[i]%k
        if reminder in hash_map:
            if i-hash_map[reminder] >= 2 :
                return True
        else:
            hash_map[reminder] = i        
    return False

print(check_good_subarray([6,2,4],6))

# The main key point in this problem is that we have to check the reminder , we check the sum just by using reminder 