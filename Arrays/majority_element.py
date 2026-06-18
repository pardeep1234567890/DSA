def majority_element():
    nums = [2,2,1,1,1,2,2]
    count = 0 
    candidate = nums[0]
    for i in range(len(nums)):
        if count == 0:
            candidate = nums[i]
        if nums[i] == candidate:
            count += 1
        else:
            count -= 1    
    return candidate
print(majority_element())