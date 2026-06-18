def arrays_intersection():
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    result= []
    mp = {}
    for num in nums1:
        mp[num] = mp.get(num,0)+1
    for num in nums2:
        if num in mp and mp[num] > 0:
            result.append(num)  
            mp[num]= mp.get(num,0)-1    #here we decrement the count 
    return result     

print(arrays_intersection())


# in this problem i did 2 mistakes that are one is i don't know how to decrease the count and how to check the count is greater than zero or not