class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        dp =[[0]*n for i in range(2)]
        if s[0] == "0":
            dp[0][0] = 0
            dp[0][1] = 1
        else:
            dp[0][0] = 1
            dp[0][1] = 0
            
        for i in range(1,n):
            if s[i] == "0":
                dp[0][i] = dp[0][i-1]
                dp[1][i] = min(dp[1][i-1],dp[0][i-1]) + 1
            else:
                dp[0][i] = dp[0][i-1] + 1
                dp[1][i] = min(dp[0][i-1],dp[1][i-1])
        
        return min(dp[0][-1],dp[1][-1])
