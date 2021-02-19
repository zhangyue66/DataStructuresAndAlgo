class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:

        ans = 0
        
        
        if len(A) <= 2:
            return ans
        
        
        for i in range(len(A)-1):
            delta = A[i+1]-A[i]
            
            for j in range(i+2,len(A)):
                
                if A[j] - A[j-1] == delta:
                    ans += 1
                else:
                    break
                    
        return ans
        https://leetcode.com/submissions/detail/457826568/?from=explore&item_id=3644
