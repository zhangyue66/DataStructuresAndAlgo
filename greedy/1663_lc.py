class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = [1]*n
        
        k -= 1*n
        
        i = n-1
        
        
        while k != 0:
            step = min(25,k)
            
            ans[i] += step
            
            k -= step
            
            i -= 1
            
            
        res = ""
        
        for a in ans:
            
            res += chr(a+96)
            
        return res
