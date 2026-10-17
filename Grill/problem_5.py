#  You're given an array of integers. Somebody took a perfectly **sorted (non-decreasing)** array and **rotated** it — they took some number of elements from the front and moved them to the back.
# > For example, `[1, 2, 3, 4, 5]` rotated by 2 becomes `[3, 4, 5, 1, 2]`.
# >
# > Given the rotated array, tell me: **was this array actually sorted and then rotated?** Return `true` or `false`. The array may contain **duplicates**.

# > Examples:
#  `[3, 4, 5, 1, 2]` → `true`
#  `[2, 1, 3, 4]` → `false`
#  `[1, 2, 3]` → `true` (rotated by 0)


# This can be solve in such a way like if the element is next element is greater more than once then we should return False else it is True 

def check_rotated(nums):
    count = 0
    n = len(nums)
    for i in range(len(nums)):
        if nums[i] > nums[(i+1)%n]:
            count += 1
    if count > 1:
        return False
    else :
        return True
print(check_rotated([2,4,5,1,2]))