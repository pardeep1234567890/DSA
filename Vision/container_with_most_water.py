# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i-th line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container that holds the
# most water. Return the maximum amount of water a container can store.

# You may not slant the container.

# Example 1:
# Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49

# The brute force approach will be like that. 
# I'm starting from the first point(i) and check this combination with all the other points and check how much water they store.
#  Then move that pointer forward(i) and then again check it with all the other points. 
# Like this I check all the combinations and check which one holds the most water. 
# Optimized task : i am choosing two pointer technique because it stops to doing the same task again and again 
# i will use max_area variable to track the max amount of water 
# if the height of left is smaller then we move left pointer 
# else i will move the right pointer and find the area and track the most water container and return the area 

def container_most_water(height):
    left = 0
    right = len(height)-1
    max_area = 0
    while left < right:
        min_height = min(height[left],height[right]) 
        width = right-left  
        area = min_height*width
        max_area = max(max_area, area) 
        if height[left] < height[right]:
            left += 1
        elif height[left] > height[right] : 
            right -= 1
        else: 
            left += 1
            right -=1
    return max_area
print(container_most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]))

# why we choose the Two Pointer Technique