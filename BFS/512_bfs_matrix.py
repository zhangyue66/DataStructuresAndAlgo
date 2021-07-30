from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        ans = [[float("inf") for i in range(n)] for j in range(m)]
        
        q = deque()
        #visited[0][0] = True
        
        def validate(row,col):
            if row < 0 or col < 0 or row >= m or col >= n:
                return False
            return True
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    ans[i][j] = 0
                    q.append((i,j))
                    
        directions =[[-1,0],[1,0],[0,-1],[0,1]] # up,down,left,right
        
        while q:
            
            row,col = q.popleft()
            
            for dr in directions:
                drow = row + dr[0]
                dcol = col + dr[1]
                if validate(drow,dcol):
                    if ans[drow][dcol] > ans[row][col] + 1:
                        ans[drow][dcol] = ans[row][col] + 1
                        q.append((drow,dcol))
                        
        return ans
