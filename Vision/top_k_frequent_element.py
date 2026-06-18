# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1, 2]

# def top_k():
#     nums = [1,1,1,2,2,3]
#     k = 2
#     hash_map = {}
#     for num in nums :
#         hash_map[num] = hash_map.get(num,0)+1
#     # now i want to sort the According to values 
#     sorted_list = sorted(hash_map , key=lambda x : hash_map[x],reverse=True)
#     return sorted_list[0:k]
# print(top_k())


def top_k(nums,k):
    hash_map = {}
    result = []
    for num in nums :
        hash_map[num] = hash_map.get(num,0)+1
    arr = [[] for _ in range(len(nums)+1)]
    for num, freq in hash_map.items():
        arr[freq].append(num)
    for i in range(len(arr)-1,-1,-1):
        if len(result) != k:
            still_need = k-len(result)
            result.extend(arr[i][:still_need])
    return result

print(top_k( [1,1,1,2,2,3],2))