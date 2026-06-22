# why not return mid instead of high ?
# The algorithm never checks during the loop whether mid is definitely the peak.
def find_peak(nums):
    low = 0
    high = len(nums)-1
    while low < high :
        mid = (low+high) //2 
        if nums[mid] < nums[mid+1]:
            low = mid+1
        else: 
            high = mid      # we include the mid because it could be the peak  
    return high             
print(find_peak([5,4,3,2,1]))    