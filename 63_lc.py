class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):

        if obstacleGrid[0][0] == 1:
            return 0

        n = len(obstacleGrid[0])
        m = len(obstacleGrid)

        obstacleGrid[0][0] = 1
        for i in range(1,n):
            if obstacleGrid[0][i] == 1:
                obstacleGrid[0][i] = 0
            elif obstacleGrid[0][i-1] != 0:
                obstacleGrid[0][i] =1
            else:
                obstacleGrid[0][i] = 0
        for j in range(1,m):
            if obstacleGrid[j][0] == 1:
                obstacleGrid[j][0] = 0
            elif obstacleGrid[j-1][0] !=0:
                obstacleGrid[j][0] = 1
            else:
                obstacleGrid[j][0] = 0

        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] != 1:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        return obstacleGrid[-1][-1]



yz = Solution()
obstacleGrid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
print(yz.uniquePathsWithObstacles(obstacleGrid))
