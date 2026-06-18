# here is the main role of the current sum
def subarray_sum():
    nums = [1,2,3]
    k = 3
    count =0
    current_sum = 0
    seen_sums = {}
    seen_sums[0] = 1 #here we write 1 because we see the 0 sum for 1 time
    for num in nums:
        current_sum = current_sum+num
        value = current_sum-k
        if value in seen_sums:
            count = count+seen_sums[value]
        seen_sums[current_sum] = seen_sums.get(current_sum,0)+1 
    return count
print(subarray_sum())        