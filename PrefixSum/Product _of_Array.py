def product_of_array():
    nums = [1,2,3,4]
    ans = []
    prefix = 1
    suffix = 1
    for i in range(len(nums)):
        ans.append(prefix)
        prefix = prefix*nums[i]
    for i in range(len(ans)-1,-1,-1):
        ans[i] = ans[i]*suffix
        suffix = suffix*nums[i]
    return ans    
print(product_of_array())
