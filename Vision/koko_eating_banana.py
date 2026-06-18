# Koko loves to eat bananas. There are n piles of bananas, the i-th pile
# has piles[i] bananas. The guards have gone and will come back in h hours.

# Koko can decide her bananas-per-hour eating speed of k. Each hour, she
# chooses some pile of bananas and eats k bananas from that pile. If the
# pile has less than k bananas, she eats all of them instead and will not
# eat any more bananas during this hour.

# Return the minimum integer k such that she can eat all the bananas within
# h hours.

# Example 1:
# Input: piles = [3, 6, 7, 11], h = 8
# Output: 4

# The main point to check the valid speed 
# the speed is depend on if the total time become not greater then the total h(hour) 
# time = ceil(p/k)

# I should use binary search here because we have a monotonic relationship and also we have a sorted array something like that. 
# we find the valid speed by adding the time takes on all piles by given speed (between 0 and max(piles)) and then check that 
# total time with given hour 

