# Which cells can send water to both the Pacific and the Atlantic ocean?
class Solution:
    def pacificAtlantic(self, heights):
        if not heights or not heights[0]:
            return 
        rows , col = len(heights) , len(heights[0])

        pacific = set()
        atlantic = set()
        def dfs(r, c, visited , prev_height):
            if (r<0 or c <0 or r >= rows or c >= col or (r,c) in visited or prev_height > heights[r][c]):
                return 
            visited.add((r,c))
            dfs(r+1,c,visited , heights[r][c])
            dfs(r-1,c,visited,heights[r][c])    
            dfs(r,c+1,visited,heights[r][c])    
            dfs(r,c-1,visited,heights[r][c])    

        # Run dfs for pacific Edges 
        for r in range(rows):
            dfs(r,0,pacific ,heights[r][0]) # left col
            dfs(r,col-1,atlantic,heights[r][col-1]) # right col
        for c in range(col):
            dfs(0,c,pacific ,heights[0][c]) # top row
            dfs(rows-1,c,atlantic,heights[rows-1][c]) # bottom row
        return list(pacific & atlantic)     