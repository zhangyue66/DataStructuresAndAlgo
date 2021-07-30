class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        dp = [[ 0 if mat[i][j] == 0 else float("inf") for j in range(n)] for i in range(m)]
        def check_distance(i,j):
            up,left,down,right = float("inf"),float("inf"),float("inf"),float("inf")
            if 0 <= i-1 < m:
                up = dp[i-1][j]
            if 0 <= j-1 < n :
                left = dp[i][j-1]
            if 0 <= i+1 < m :
                down = dp[i+1][j]
            if 0 <= j+1 < n:
                right = dp[i][j+1]
            
            min_d = min(up,left,down,right) + 1
            return min(min_d,dp[i][j])
                
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = check_distance(i,j)
                    
        #reverse from last node to first node
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                dp[i][j] = check_distance(i,j)
                
        return dp
