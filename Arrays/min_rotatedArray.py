# this is just the implementation fo the Binary search 
def min_rotated_array():
    nums = [3,4,5,1,2]
    low = 0
    n = len(nums)
    high = n-1
    while low < high:
        mid = (low + high) // 2
        if(nums[mid] > nums[high]):
            low = mid+1
        else:
            high = mid
    return nums[low] 
print(min_rotated_array())