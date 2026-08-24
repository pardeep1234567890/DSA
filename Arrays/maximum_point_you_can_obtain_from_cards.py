# 1423. Maximum Points You Can Obtain from Cards
# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.


# Example 1:
# Input: cardPoints = [1,2,3,4,5,6,1], k = 3
# Output: 12
# Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
# Example 2:

# Input: cardPoints = [2,2,2], k = 2
# Output: 4
# Explanation: Regardless of which two cards you take, your score will always be 4.
# Example 3:

def max_point_obtain(cardPoints,k):
    sub_array = cardPoints[0:k]
    total_sum = 0
    for num in sub_array:
        total_sum = total_sum+num
    max_sum = total_sum
    left = k-1
    right = len(cardPoints)-1
    for i in range(k):
        total_sum = total_sum - cardPoints[left] +cardPoints[right]
        max_sum = max(total_sum, max_sum)
        left -=1
        right -=1
    return max_sum
print(max_point_obtain([1,2,3,4,5,6,1],3))