from itertools import combinations
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        i,j = len(s),len(t)
        dp = [[0 for x in range(j+1)] for y in range(i+1)]
        # padding first col to all 1s
        for y in range(i+1):
            dp[y][0] = 1
        for y in range(1,i+1):
            for x in range(1,j+1):
                if s[y-1] == t[x-1]:
                    dp[y][x] = dp[y-1][x] + dp[y-1][x-1]
                else:
                    dp[y][x] = dp[y-1][x]
        #print(dp)
        return dp[-1][-1]
