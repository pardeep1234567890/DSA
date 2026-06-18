def permute(nums):
    result = []
    path = []
    def backtrack():
        if len(path) == len(nums):
            result.append(path[:])
            return
        for num in nums:
            if num in path:
                continue
            path.append(num)
            backtrack()
            #backtrack
            path.pop()

    backtrack()
    return result

print(permute([1,2]))