from math import ceil
def koko_eat_banana(piles,h):
    low= 1
    high= max(piles)
    result = high
    while low <= high: # because we want the exact value 
        mid = (low + high) //2 # if we have to return k so we return it as mid and also mid is like the exact speed of k and if it is greater than h then k is too slow we move to high side 
        total_time = sum(ceil(pile/mid) for pile in piles)   #It's a Python shorthand called generator expression
        if total_time <= h :     # here hours are valid so we check for the more smaller value of k and move tp left side
            result = mid
            high = mid-1
        else:
            low = mid+1    
    return result
print(koko_eat_banana([30,11,23,4,20],5))    