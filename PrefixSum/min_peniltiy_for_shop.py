# 2483. Minimum Penalty for a Shop
# You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

# if the ith character is 'Y', it means that customers come at the ith hour
# whereas 'N' indicates that no customers come at the ith hour.
# If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
# For every hour when the shop is open and no customers come, the penalty increases by 1.
# For every hour when the shop is closed and customers come, the penalty increases by 1.
# Return the earliest hour at which the shop must be closed to incur a minimum penalty.

# Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.


# Example 1:

# Input: customers = "YYNY"
# Output: 2
# Explanation: 
# - Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
# - Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
# - Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
# - Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
# - Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
# Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.

# should i check maximum N 
# like after j point N should be max and Y should be less 

# def min_pen_for_shop(customers):
#     best_hour = 0
#     penality  = 0
#     min_pen = float("+inf")
#     for i in range(len(customers)):
#         if customers[i] == "N":
#             penality += 1
#     if penality< min_pen:
#         min_pen = penality
#         best_hour = len(customers)
#     for i in range(len(customers)-1,-1,-1):
#         if customers[i]=="Y":
#             penality += 1
#         else :
#             penality -=1 
#         if penality <= min_pen:
#             min_pen = penality
#             best_hour = i
#     return best_hour 


# print(min_pen_for_shop("YYYY"))


def min_pen_for_shop(customers):
    score = 0
    min_score = 0 
    best_hour = 0
    for i in range(len(customers)):
        if customers[i]== "Y":
            score -=1 
        else :
            score +=1
        if min_score > score:
            min_score = score
            best_hour = i+1  # because i am choosing to decide to close at next hour 
    return best_hour
print(min_pen_for_shop("YYNY"))