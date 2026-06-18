def containsDuplicate():
    nums = [1,2,3,4]
    s = set()
    for item in nums:
        if item in s:
            return True
        s.add(item)
    return False
print(containsDuplicate())