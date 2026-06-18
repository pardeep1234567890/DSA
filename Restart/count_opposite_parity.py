def count_opposite_parity ():
    arr = [1,2,3,4]
    total_even = 0
    total_odd = 0
    prefix_even = 0
    prefix_odd = 0 
    ans = [0]*len(arr)
    for num in arr : 
        if num % 2 == 0 :
            total_even += 1
        elif num % 2 !=0 :
            total_odd +=1    
    for i in range(len(arr)) :
        if arr[i] %2 == 0:
            future_odd = total_odd-prefix_odd 
            ans[i] = future_odd
            prefix_even += 1
        else : 
            future_even = total_even-prefix_even
            ans[i] = future_even
            prefix_odd += 1
    return ans    

print(count_opposite_parity())    