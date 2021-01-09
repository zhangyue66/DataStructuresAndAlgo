class Solution:
    def numTrees(self, n: int) -> int:
        #DP method DP[i,n] = DP[i-1]*DP[n-i]
        if n ==1 :
            return 1

        dp = [1]* (n+1)

        for i in range(2,n+1):
            total = 0
            for j in range(1,i+1):
                temp = dp[j-1]*dp[i-j]

                total += temp

            dp[i] = total

        return dp[-1]

yz = Solution()
n = 4
print(yz.numTrees(n))
