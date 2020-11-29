class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return 

        m = len(board)   #x
        n = len(board[0]) #y

        parent =[i for i in range(m*n+1)]
        #print(parent)

        def find(a):
            if a == m*n:
                return m*n

            if parent[a] == a:
                return a
            return find(parent[a])

        def union(a,b):
            pa = find(a)
            pb = find(b)
            
            if pa == m*n:
                parent[pb] = m*n
            if pb == m*n:
                parent[pa] = m*n
            if pa != pb:
                parent[pa] = pb

        for i in range(m):
            if board[i][0] == "O":
                union(i*n,m*n)
            if board[i][n-1] == "O":
                union(i*n+n-1,m*n)

        for j in range(n):
            if board[0][j] == "O":
                union(j,m*n)
            if board[m-1][j] == "O":
                union(n*(m-1)+j,m*n)
                
        #print(parent)

        direction = [[1,0],[0,1],[0,-1],[-1,0]]

        for i in range(1,m-1):
            for j in range(1,n-1):
                if board[i][j] == "O":
                    for k in range(4):
                        x = i + direction[k][0]
                        y = j + direction[k][1]
                        if board[x][y] == "O":
                            #print(x*n+y,i*n+j)
                            union(x*n+y,i*n+j)
                            
        #print(parent)
        
        for i in range(1,m-1):
            for j in range(1,n-1):
                if find(i*n+j) != m*n:
                    board[i][j] = "X"
