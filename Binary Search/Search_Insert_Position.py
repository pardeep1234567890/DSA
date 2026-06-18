# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
def search_insert(nums,target):
    low =0
    high = len(nums)-1
    while low <= high: # because we want the exact value 
        mid = (low+high) //2
        if target>nums[mid] :
            low = mid +1
        elif target < nums[mid]:
            high = mid -1
        else:
            return mid
    return low    

print(search_insert([1,3,5,6],2))   