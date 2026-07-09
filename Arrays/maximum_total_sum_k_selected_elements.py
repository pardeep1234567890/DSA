def maxSum(nums, k, mul):
    total_sum = 0
    sorted_nums = sorted(nums,reverse=True)
    new_nums = sorted_nums[0:k]
    for i in range(len(new_nums)):
        if mul>1:
            total_sum += new_nums[i]*mul
        else :
            total_sum += new_nums[i]
        mul -=1
    return total_sum
print(maxSum([3,7,5,2],2,4))