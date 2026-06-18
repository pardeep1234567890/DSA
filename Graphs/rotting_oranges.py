from collections import deque
class Solution:
    def orangesRotting(self, grid):
        queue = deque([])
        fresh_count = 0
        row, col = len(grid),len(grid[0])
        time = -1
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh_count += 1  
        if fresh_count == 0 :
            return 0              
        while queue :
            level_length=len(queue)
            for i in range(level_length):
                level_row , level_col = queue.popleft()
                
                directions = [(1,0), (-1,0), (0,1), (0,-1)]

                for dr , dc in directions:
                    nr , nc = level_row+dr , level_col + dc
                    if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -=1 
                        queue.append((nr,nc))
            time +=1
        if fresh_count == 0:
            return time
        else:
            return -1    