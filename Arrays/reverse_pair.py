# 493. Reverse Pairs
# Given an integer array nums, return the number of reverse pairs in the array.
# A reverse pair is a pair (i, j) where:

# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].
 

# Example 1:

# Input: nums = [1,3,2,3,1]
# Output: 2
# Explanation: The reverse pairs are:
# (1, 4) --> nums[1] = 3, nums[4] = 1, 3 > 2 * 1
# (3, 4) --> nums[3] = 3, nums[4] = 1, 3 > 2 * 1




def reverse_pairs(nums):
    def Merge_sort(nums,left,right):
        if left >= right :
            return 0
        mid = (left+right) // 2
        count = Merge_sort(nums,left,mid)
        count += Merge_sort(nums,mid+1,right)
        count += Count_cross_pair(nums,left,mid,right)

        Merge(nums,left,mid, right)
        return count
    
    def Merge(nums,l,mid,r):
        a = []
        b = []
        for i in range(l , mid+1):
            a.append(nums[i])
        for i in range(mid+1,r+1):
            b.append(nums[i])
        i,j,k = 0,0,l 
        while k<=r :
            if j == len(b):
                nums[k] = a[i]
                i +=1
                k+=1
            elif i == len(a):
                nums[k] = b[j]
                j +=1
                k+=1
            elif a[i] < b[j]:
                nums[k] = a[i]
                i+=1
                k+=1
            else : 
                nums[k] = b[j]
                j+=1
                k+=1
         
    def Count_cross_pair(nums,l,mid,r):
        count = 0
        j = mid+1
        for i in range(l,mid+1):
            while j<= r and nums[i]> 2*nums[j]:
                j+=1
            count += (j-(mid+1))
        return count 
    return Merge_sort(nums,0,len(nums)-1)






    


