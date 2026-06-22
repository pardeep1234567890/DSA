# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

# this is the main thing what we need 
#  You need to find the longest contiguous subarray that contains at most 2 distinct values. Does that match your understanding?

# use sliding window
# and shrink the window when the thrid different value appears 
# hashing can be used to store how many distinct types of fruit in my window 

# The hashmap stores the key as the fruit type(integer array) and value as frequency 
# when shrinking : 

def fruit_into_basket(fruits):
    left = 0
    hash_map = {}
    max_fruits = 0
    for right in range(len(fruits)):
        hash_map[fruits[right]] = hash_map.get(fruits[right],0)+1
        while len(hash_map) > 2:
            hash_map[fruits[left]] = hash_map.get(fruits[left],0)-1
            if hash_map[fruits[left]] ==0 :
                del hash_map[fruits[left]]
            left += 1
        max_fruits = max(max_fruits,right-left+1)
    return max_fruits
print(fruit_into_basket([1,2,3,2,2]))