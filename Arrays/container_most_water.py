#  this is the two pointer technique , we keep one pointer at starting pointt and other at end point 
def container_most_water():
    nums = [1,1]
    left = 0
    right = len(nums)-1
    area =0 
    while left <right:
        # here we find the area
        new_area = min(nums[left],nums[right])*(right-left)
        # here we find the maximum are
        if new_area > area:
            area = new_area
        # here we use gready approach that which height is greater 
        if(nums[left]<nums[right]):
            left = left+1
        else:
            right = right-1
    return area
print(container_most_water())             
