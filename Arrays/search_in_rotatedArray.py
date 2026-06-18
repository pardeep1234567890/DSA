# this code is similar to the find minimum in rotated array but in that case we check only the right half b/z the minimum is in the rotated part 
# but in this we find the target index so we check both the halfs that these are sorted or not 
def search_in_rotated_array():
    nums = [4,5,6,7,0,1,2]
    target = 0
    low = 0
    high = len(nums)-1
    while low <= high :
        mid = (low+high) //2
        if nums[mid] == target:
            return mid
        # here we check if the left half is sorted or not
        if (nums[low]<=nums[mid]):
            # if the left half is sorted now we check that the target is in the left half or not 
            if(target >= nums[low] and target < nums[mid]):  # Use <= or >= when you want to include the boundary value in your range
                high = mid-1
            else:
                low = mid+1     
        # If left half is not sorted, then right half must be sorted.
        else:
            if(target > nums[mid] and target <= nums[high]):
                low = mid+1
            else:
                high = mid-1    
    return -1                                   
print(search_in_rotated_array())