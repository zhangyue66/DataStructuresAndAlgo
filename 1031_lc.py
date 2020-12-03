class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        if L+M > len(A):
            return 0
        
        presum = []
        sum = 0
        for a in A:
            sum += a
            presum.append(sum)
            
        ans,max_L,max_M = presum[L+M-1],presum[L-1],presum[M-1]
        #print(presum)
        for i in range(L+M,len(A)):
            max_L = max(max_L,presum[i-M]-presum[i-L-M])
            max_M = max(max_M,presum[i-L]-presum[i-L-M])
            
            #res = max(front, back)
            res = max(max_L+presum[i]-presum[i-M],max_M+presum[i]-presum[i-L])
            ans = max(ans,res)
            
        return ans
