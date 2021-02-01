class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        
        for i in bin(n):
            if i == "1":
                ans += 1
        
        return ans
