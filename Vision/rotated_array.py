#the main idea is we have to check the smaller side 
#  The main outline of this problem is:
# 1. We check the mid element from the last point.
# 2. This will be: if mid is greater than high then we move low.
# 3. If the mid is lower then we move high.

# the main idea is simple like we check the smaller element the right side (because the array is rotated and we find smaller elemet that side )
def find_min(nums):
    low = 0
    high = len(nums)-1
    while low < high :
        mid = (low+high) //2
        if nums[mid] > nums[high]:
            low = mid+1
        else :
            high = mid 
    return nums[low]
print(find_min([4,5,6,7,0,1,2]))