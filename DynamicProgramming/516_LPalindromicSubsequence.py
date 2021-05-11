class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # if len(s) <= 1:
        #     return 1
        n = len(s)
        # dp[l][r]  left index and right index
        #if s[l] == s[r] dp[i][j] = 2+dp[i+1][j-1]
        #else dp[i][j] = max(dp[i+1][j],dp[i][j-1])
        dp = [[0 for i in range(n)] for j in range(n)]
        for l in range(1,n+1):
            for i in range(0,n-l+1):
                # left index = i
                # right index = j = i+l-1
                j = i+l-1
                if i == j:
                    dp[i][j] = 1
                    continue
                # if i > j :
                #     continue
                    
                if s[i] == s[j] :
                    dp[i][j] = 2+dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j-1])
                    
        #print(dp)
        return dp[0][n-1]
                
                
