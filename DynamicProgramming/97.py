class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False 
        
        m,n = len(s1),len(s2)
        # use a padding in front of each s1 and s2 string
        s1 = "#" + s1
        s2 = "#" + s2
        s3 = "#" + s3
        dp = [[False for i in range(n+1)] for j in range(m+1)]
        dp[0][0] = True
        for i in range(1,m+1):
            dp[i][0] = (dp[i-1][0] == True and s1[i] == s3[i])
        for j in range(1,n+1):
            dp[0][j] = (dp[0][j-1] == True and s2[j] == s3[j])
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i] == s3[i+j] and dp[i-1][j] == True:
                    dp[i][j] = True
                elif s2[j] == s3[i+j] and dp[i][j-1] == True:
                    dp[i][j] = True
                    
        return dp[-1][-1]
