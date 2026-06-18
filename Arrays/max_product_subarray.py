def max_product():
    nums = [2,3,-2,4]
    current_max = nums[0]
    current_min =  nums[0]
    result = nums[0]
    for i in range(1,len(nums)):
        current_max , current_min = max(nums[i],nums[i]*current_max,nums[i]*current_min),min(nums[i],nums[i] *current_max,nums[i] *current_min)
        result = max(current_max,result)                
    return result
print(max_product())