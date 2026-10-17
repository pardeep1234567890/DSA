# 204. Count Primes
# Given an integer n, return the number of prime numbers that are strictly less than n.
# Example 1:

# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# Example 2:

# Input: n = 0
# Output: 0
# Example 3:

# Input: n = 1
# Output: 0

# def count_prime(n):
#     count = 0
#     def is_prime(num):
#         for i in range(2,num):
#             if num % i == 0:
#                 return False 
#         return True
#     for i in range(2,n):
#         if is_prime(i) == True:
#             count +=1
#     return count

def count_prime(n):
    if n<= 1:
        return 0
    primes = n *[True]
    primes[0] = False
    primes[1] = False

    for i in range(2,n):
        if primes[i] == True:
            for multiple in range(i*2,n,i):
                primes[multiple] = False
    count = 0
    for prime in primes:
        if prime == True: 
            count+=1
    return count


# class Solution(object):
#     def countPrimes(self, n):
#         if n <= 2:
#             return 0

#         # Assume every number is prime initially
#         isPrime = [True] * n
#         isPrime[0] = isPrime[1] = False

#         # Mark multiples of each prime as non-prime
#         p = 2
#         while p * p < n:
#             if isPrime[p]:
#                 for multiple in range(p * p, n, p):
#                     isPrime[multiple] = False
#             p += 1

#         return sum(isPrime)


