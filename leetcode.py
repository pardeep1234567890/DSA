# Q1. Even Number of Knight Moves
# You are given two integer arrays start and target, where each array is of the form [x, y] representing a cell on a standard 8 x 8 chessboard.
# Return true if a knight can move from start to target in an even number of moves. Otherwise, return false.
# Note: A valid knight move consists of moving two squares in one direction and one square perpendicular to it. The figure below illustrates all eight possible moves from a cell.

def canReach(start, target):
    # x1,y1 = [item for item in start]
    # x2,y2 = [item for item in target]
    x1 , y1 = start 
    x2,y2 = target 
    x = x1+y1
    y = x2+y2
    if x %2 == y %2:
        return True 
    else :
        return False

# To see the optimization, think about the visual pattern of a standard chessboard. It consists of alternating black and white squares.
# Imagine your knight starts on a White square:
# What color square will it land on after exactly 1 move? ans = 1. on the opposite color
# What color square will it be on after 2 moves? ans = 2. on the same color from where it started 

# Bingo! You nailed it. The color of any square on a chessboard is entirely determined by whether the sum of its coordinates (x + y) is even or odd.
# If two squares are the same color, their coordinate sums will either both be even, or both be odd. In other words, they will have the same parity.
# Now, let's put it all together! How would you write the logic in Python to return True if start and target are the same color, and False otherwise?