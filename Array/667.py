class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans =[i for i in range(1,n+1)]
        
        rev = 1
        
        while rev < k:
            ans[rev::] = ans[rev::][::-1]
            rev += 1
            
        return ans
            
            
