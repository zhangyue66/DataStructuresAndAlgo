class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        # at each point of matrix, find its longest increasing path , use greedy to compare with ans
        # use dfs(node) to find length
        self.ans = 1
        m,n = len(matrix),len(matrix[0])
        memorization =[[0 for i in range(n)] for j in range(m)]

        # directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        def dfs(i,j,directions,m,n):
            if memorization[i][j] > 0:
                return memorization[i][j]
            step = 1
            for dir in directions:
                if 0<=i+dir[0]<m and 0<=j+dir[1]<n and matrix[i][j] < matrix[i+dir[0]][j+dir[1]]:
                    later = dfs(i+dir[0],j+dir[1],directions,m,n)+1
                    step = max(step,later)
            memorization[i][j] = step
            return step
                                        
        for i in range(m):
            for j in range(n):
                # matrix[m][n] ->direction
                
                directions = [(0,1),(0,-1),(1,0),(-1,0)]
                self.ans = max(self.ans,dfs(i,j,directions,m,n))
                
        return self.ans
        
        
