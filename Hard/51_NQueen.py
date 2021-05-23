class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = [0]*n
        diag1 = [0]*(2*n-1)  #   /////
        diag2 = [0]*(2*n-1)  #    \\\\\
        
        res = []
        board = [["." for i in range(n)] for j in range(n)]
        
        def available(x,y):
            if cols[x]==0 and diag1[x+y]==0 and diag2[x-y+n-1]==0:
                return True
            return False
        
        def putChessOnBoard(x,y):
            cols[x] = 1
            diag1[x+y] = 1
            diag2[x-y+n-1] = 1
            board[x][y] = "Q"
        
        def removeChess(x,y):
            cols[x] = 0
            diag1[x+y] = 0
            diag2[x-y+n-1] = 0
            board[x][y] = "."
        
        def backtrack(y,n,res):
            if y == n:
                temp = []
                for col in board[:]:
                    temp.append("".join(col))
                res.append(temp)
                return         
            for x in range(n):
                if not available(x,y):
                    continue
                putChessOnBoard(x,y)
                backtrack(y+1,n,res)
                removeChess(x,y)
                
        backtrack(0,n,res)
        
        return res
        
