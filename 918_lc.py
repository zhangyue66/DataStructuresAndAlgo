class Solution:
    def maxSubarraySumCircular(self, A):
        sumTotal = sum(A)

        #Use Kadane to get Max Subarray
        maxTotal = A[0]
        total = A[0]
        for i in range(1,len(A)):
            total = max(A[i],A[i]+total)
            maxTotal = max(maxTotal,total)

        #Use Kadane to get Min Subarray
        minTotal = A[0]
        min_total = A[0]
        for i in range(1,len(A)):
            min_total = min(min_total,A[i]+min_total)
            minTotal = min(minTotal,min_total)


        if maxTotal <0 :
            return maxTotal
        return max(maxTotal,sumTotal-minTotal)


A = [1,-2,3,-2]
yz = Solution()
print(yz.maxSubarraySumCircular(A))
