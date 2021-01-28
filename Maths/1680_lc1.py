class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = ""
        
        for i in range(1,n+1):
            ans += (bin(i))[2::]       
        ans = int(ans,2)
        return ans%(10**9+7)
