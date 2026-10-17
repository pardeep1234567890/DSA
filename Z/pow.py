# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
# Example 1:

# Input: x = 2.00000, n = 10
# Output: 1024.00000

# i will use binary exponention to solve this problem in iterative way : means calculate the answer by converting the power into binary form 
# using Iterative Approach 
def pow(x , n):
    if n < 0 :
        x = 1/x
        n = -n 
    result = 1
    while n > 0 : 
        if n%2 != 0 :   # i was very confused here like i didn't identify that to get the binary digit we use n%2 instead of n%10(whcih we use in case of decimal numbers) 
            result = x * result 
        x = x * x
        n = n // 2
    return result 
print(pow(2,-3))


#  Any code will be submitted successfullly when it contains Atmost 10^8 operations. 