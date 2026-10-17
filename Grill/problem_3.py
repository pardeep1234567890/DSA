# You're given an integer array nums. Find the contiguous subarray (containing at least one number) that has the largest product, and return that product.
# Example: nums = [2, 3, -2, 4] → answer is 6 (subarray [2, 3])

# Example: nums = [-2, 0, -1] → answer is 0


def largestProduct(nums):
    max_product = nums[0]
    min_product = nums[0]
    global_max = nums[0]
    for i in range(1,len(nums)):
        max_product ,min_product= max(nums[i],nums[i]*max_product,nums[i]*min_product), min(nums[i],nums[i]*max_product,nums[i]*min_product)
        global_max = max(max_product,min_product,global_max)
    return global_max
print(largestProduct([-3]))


# but if there is Two negative number then it makes the product positive also 
# so i can't skip the negative numbers
# How to count the negative number , like if the count of negative number are even then no problem but when the count 
# but if the count is odd then it become the problamatic thing , so if the count is odd what should i do like where should i start the window 
# i can do this by track the last index of the neg value and at the end if the count is odd then left index will be that last negative value 
# but what if the product of left side of the negative value is max in that case i can do one thing like keep the product till the first negative number then continue including the negative numbers 


# so the solution of my all contradiction here is to also maintain the minimum product also because if in future there will chance that any negative number comes and increase the product 

