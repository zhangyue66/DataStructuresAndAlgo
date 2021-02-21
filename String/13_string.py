class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        # I, V, X, L, C, D and M.
        # 1, 5, 10,50,100,500 and 1000
        dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        
        prev = None
        
        for i in range(len(s)-1,-1,-1):
            if prev is None: # first one , no need to check
                ans += dict[s[i]]
                prev = dict[s[i]]
            else:
                cur = dict[s[i]]
                if cur < prev:
                    ans -= cur
                else:
                    ans += cur
                    
                prev = cur
                
        return ans
