# You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.
# Return the index of the peak element.
# Your task is to solve it in O(log(n)) time complexity.

def peak_index_in_mountain_array(arr):
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = (left+right) //2 
        if arr[mid] > arr[mid+1] and arr[mid] >arr[mid-1]:
            return mid
        elif arr[mid] < arr[mid+1]:
            left = mid+1
        else :
            right = mid -1 
print(peak_index_in_mountain_array([0,1,2,3,2,1,0]))
# ---------------------------------------------------------
def peak_index_in_mountain_array(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        mid = (left+right) //2 
        if arr[mid] < arr[mid+1]:
            left = mid+1
        else:
            right = mid
    return left
print(peak_index_in_mountain_array([0,1,2,3,2,1,0]))