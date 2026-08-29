# 1927. Sum Game
# Alice and Bob take turns playing a game, with Alice starting first.
# You are given a string num of even length consisting of digits and '?' characters. On each turn, a player will do the following if there is still at least one '?' in num:
# Choose an index i where num[i] == '?'.
# Replace num[i] with any digit between '0' and '9'.
# The game ends when there are no more '?' characters in num.
# For Bob to win, the sum of the digits in the first half of num must be equal to the sum of the digits in the second half. For Alice to win, the sums must not be equal.

# For example, if the game ended with num = "243801", then Bob wins because 2+4+3 = 8+0+1. If the game ended with num = "243803", then Alice wins because 2+4+3 != 8+0+3.
# Assuming Alice and Bob play optimally, return true if Alice will win and false if Bob will win.
 

# Example 1:

# Input: num = "5023"
# Output: false
# Explanation: There are no moves to be made.
# The sum of the first half is equal to the sum of the second half: 5 + 0 = 2 + 3

# def sum_game(num):
#     q1,q2,sum1,sum2  = 0,0,0,0
#     mid = len(num)//2
#     for i in range(len(num)):
#         if i == mid :
#             if num[mid] != "?":
#                 sum2 += int(num[i])
#             else : 
#                 q2 +=1
#         if i<mid and num[i] == "?":
#             q1 += 1
#         elif i > mid and num[i] == "?":
#             q2 +=1
#         else:
#             if i<mid :
#                 sum1 += int(num[i])
#             else:
#                 sum2 += int(num[i])
        



# print(sum_game("25??"))


def sum_game(num):
    q1,q2,sum1,sum2  = 0,0,0,0
    mid = len(num)//2
    for i in range(len(num)):
        if i < mid :
            if num[i] == "?":
                q1 +=1
            else :
                sum1 += int(num[i])
        else:
            if num[i] == "?":
                q2 +=1
            else :
                sum2 += int(num[i])
    total_q = q1+q2 
    if total_q%2 != 0 :
        return True
    else :
        if sum1+9*(q1/2) == sum2+9*(q2/2):
            return False
        else :
            return True
        



print(sum_game("25??"))