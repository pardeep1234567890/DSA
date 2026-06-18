class Solution:
    def solve(self, board):
        if not board or not board[0]:
            return None
        rows , col = len(board),len(board[0])    

        def dfs(r,c):   
            if r<0 or r>=rows or c<0 or c>= col or board[r][c] != "O":
                return 
            board[r][c] ="T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        # Mark all Zeros connected to border
        for r in range(rows) :
            dfs(r,0) #first column 
            dfs(r,col-1) #last column 
        for c in range(col) :    
            dfs(0,c)
            dfs(rows-1,c)
        # Flip the surrounded 0
        for r in range(rows) :
            for c in range(col):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"        