class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        #Think dynamic programming: dp[i] will be the answer for array A[0], ..., A[i-1].
        #For j = 1 .. k that keeps everything in bounds, dp[i] is the maximum of dp[i-j] + max(A[i-1], ..., A[i-j]) * j .
        dp = [0] * (len(arr)+1)

        # dp[i] = dp[i-1]+arr[i]*1 -> dp[i-k] + max (A[i-k+1])*k

        for i in range(1,len(arr)+1):
            maxi = 0
            for j in range(1,min(k,i)+1):
                maxi = max(maxi,arr[i-j])
                dp[i] = max(dp[i],dp[i-j]+maxi*j)


        return dp[-1]


yz = Solution()
arr = [1,15,7,9,2,5,10]
k = 3
print(yz.maxSumAfterPartitioning(arr,k))
