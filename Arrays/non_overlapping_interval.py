# 435. Non-overlapping Intervals
# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
# Note that intervals which only touch at a point are non-overlapping. For example, [1, 2] and [2, 3] are non-overlapping.


# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

# def non_overlapping(intervals):
#     sorted_arr = sorted(intervals)
#     result = [sorted_arr[0]]
#     for i in range(1,len(intervals)):
#         if result[-1][1] > intervals[i][0]:
#             result[-1][1] = max(intervals[i][1],result[-1][1])
#         else :
#             result.append(intervals[i])
#     return result
    


# print(non_overlapping([[1,2],[2,3],[3,4],[1,3]]))

def non_overlapping(intervals):
    if not intervals:
        return 0
    sorted_arr = sorted(intervals)
    rem_count = 0
    prev_end = sorted_arr[0][1]
    for i in range(1,len(sorted_arr)):
        if prev_end > sorted_arr[i][0]:
            rem_count +=1 
            prev_end = min(prev_end,sorted_arr[i][1])
        else :
            prev_end = sorted_arr[i][1]
    return rem_count

print(non_overlapping([]))