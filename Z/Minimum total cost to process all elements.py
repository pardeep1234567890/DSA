# You are given an integer array nums and an integer k.
# Initially, you have k units of resources.
# You must process the elements of nums from left to right. To process the ith element, you need nums[i] resources.
# If your available resources are less than nums[i], you may perform an operation that increases your available resources by k. The value of k is fixed and does not change throughout the process. The first such operation incurs a cost of 1, the second incurs a cost of 2, and so on.
# After processing the ith element, your available resources decrease by nums[i].
# Return an integer denoting the minimum total cost required to process all elements. Since the answer may be very large, return it modulo 109 + 7.

 

# Example 1:
# Input: nums = [1,2,3,4], k = 4
# Output: 3

# Explanation:

# After processing nums[0], we have 4 - 1 = 3 units of resources left.
# After processing nums[1], we have 3 - 2 = 1 unit of resources left.
# Since nums[2] = 3 and only 1 unit of resources is available, we perform the first operation costing 1. After processing nums[2], we have 1 + 4 - 3 = 2 units of resources left.
# Since nums[3] = 4 and only 2 units of resources are available, we perform the second operation costing 2, to have 2 + 4 = 6 units of resources, which is enough to process nums[3].
# Thus, the total cost is 1 + 2 = 3.


def minCost(nums,k):
    MOD = 10**9 + 7
    current_unit = k
    operation_count =0
    total_cost= 0
    for num in nums :
        while current_unit<num:
            operation_count +=1 
            total_cost = (total_cost+ operation_count)% MOD
            current_unit += k
        current_unit = current_unit- num
    return total_cost
print(minCost([1,1,7,14], 4))
