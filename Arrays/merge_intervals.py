# 56. Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi],
#  merge all overlapping intervals, and return an array of the 
# non-overlapping intervals that cover all the intervals in the input.

def merge(intervals):
    sort_intervals = sorted(intervals)
    result = [sort_intervals[0]]
    for i in range(1,len(sort_intervals)):
        if result[-1][1]>= sort_intervals[i][0]:
            result[-1][1] = max(result[-1][1],sort_intervals[i][1]) 
        else :
            result.append(sort_intervals[i])
    return result
    


print(merge([[1,3],[2,6],[8,10],[15,18]]))

# class Solution(object):
    
#     def merge(self, intervals):
#         """
#         :type intervals: List[List[int]]
#         :rtype: List[List[int]]
#         """
#         if not intervals: return []
#         intervals.sort(key=lambda x: x[0])
#         new_array = []

#         current_compare = intervals[0]

#         for x in intervals:
#             if x[0] <= current_compare[1] and x[1] >= current_compare[1]:
#                 current_compare[1] = x[1]
#             elif x[0] > current_compare[1]:
#                 new_array.append(current_compare)
#                 current_compare = x
        
#         new_array.append(current_compare)
#         return new_array