class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp =[[0 for i in range(n)] for j in range(m)]
        dp[0][0] =1
        for i in range(m):
            for j in range(n):
                if i == 0 and j ==0:
                    continue
                if obstacleGrid[i][j] == 0:
                    left,top = 0,0
                    if j-1>= 0:
                        left = dp[i][j-1]
                    if i-1 >=0:
                        top = dp[i-1][j]
                        
                    dp[i][j] = left+top
                    
                else:
                    dp[i][j] = 0
                    
        return dp[-1][-1]
        
        
