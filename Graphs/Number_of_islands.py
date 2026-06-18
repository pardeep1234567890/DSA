# Three Step Solution 
# 1. Initialization 
# 2. Helper Function :- to mark the nodes as visited and check the land cells connected to the current land cell
# 3. For Loop :- This is not the another part , it's just the main function part to move to the every node if not visited and we use this 
# because there could the nodes(island) that are are seperated to the one island 
class Solution:
    def numIslands(self, grid):
        # Initialization 
        visited = set()
        island = 0
        rows, cols = len(grid), len(grid[0])

        # Helper function that explores and marks all connected land cells (the entire island) as visited using DFS
        def dfs(r, c):
            if r<0 or r>= rows or c<0 or c>=cols or grid[r][c] == "0" or (r,c) in visited:
                return   
            visited.add((r,c))    
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        # here we use loop for every row and col check (This is the part of the main Loop)
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    island +=1
                    dfs(r,c)
        return island