# def max_subarray():
#     nums = [-2,1,-3,4,-1,2,1,-5,4]
#     max_sum = nums[0]
#     current_sum = nums[0]
#     for i in range(1,len(nums)):
#         current_element = nums[i]
#         if current_sum < current_element:
#             current_sum = current_element
#         if current_sum > current_element:
#             current_sum = current_sum + current_element
#         if current_sum >max_sum:
#             max_sum = current_sum
#     return max_sum
# print(max_subarray())


def max_subarray():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum

print(max_subarray())
