def binary_search(nums,target):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = (low +high) //2
        if nums[mid] == target :
            return mid 
        elif target >= nums[mid]:
            low = mid +1
        else:
            high = mid -1
    return -1
    
print(binary_search([1,2,3,4,5],6))