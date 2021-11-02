class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        self.ans = 0
        blocks = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    #this is the start point
                    start = (i,j)
                if grid[i][j] == 0:
                    blocks += 1
        def dfs(x,y,blocks):
            if 0<=x<m and 0<=y<n and grid[x][y] >=0:
                
                if grid[x][y] == 2:
                    if blocks+1 == 0:
                        self.ans += 1
                    return
                grid[x][y] = -2
                directions =[(-1,0),(1,0),(0,-1),(0,1)]
                for dx,dy in directions:
                    dfs(x+dx,y+dy,blocks-1)
                grid[x][y] = 0
        x,y = start
        #print(x,y,blocks)
        dfs(x,y,blocks)
        return self.ans
