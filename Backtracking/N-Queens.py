def NQueens(n):
    result = []
    used_col = set() 
    used_positive_diagonals = set()
    used_negative_diagonals = set()
    chess_board = ["."*n for _ in range(n)]
    def backtrack(row):
        # here i will define the base case 
        if row == n :
            result.append(chess_board[:])
            return 
        # here we apply the loop to change the col means if the queen is in attack col in the particular row then we continue and move to the next col 
        for col in range(n):
            if col in used_col or (row-col) in used_positive_diagonals or (row+col) in used_negative_diagonals:
                continue
            # here we place the queen on board 
            row_list = list(chess_board[row])
            row_list[col] = "Q"
            chess_board[row] = "".join(row_list)    # i don't understand the working of this line 
            # here we update the sets
            used_col.add(col)
            used_positive_diagonals.add(row-col)
            used_negative_diagonals.add(row+col)
            # here i define the recursion
            backtrack(row+1)
            # now i am define the backtrack if base case hit 
            used_col.remove(col)
            used_positive_diagonals.remove(row-col)
            used_negative_diagonals.remove(row+col)
            row_list = list(chess_board[row])
            row_list[col] = "."
            chess_board[row]= "".join(row_list)
    backtrack(0)
    return result
print(NQueens(4))