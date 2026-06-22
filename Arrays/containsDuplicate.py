def containsDuplicate():
    nums = [1,2,3,4]
    s = set()
    for item in nums:
        if item in s:
            return True
        s.add(item)
    return False
print(containsDuplicate())

# the approach is simple we apply the loop on the array and add the number in the set if it is not in set already,
#  if it is in the set already then we return true else we return false after completing the loop 
# 