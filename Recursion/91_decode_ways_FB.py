class Solution:
    def numDecodings(self, s: str) -> int:
        # recursion with memorization
        if len(s) == 0:
            return 0
        
        memo = {"":1}
        @lru_cache
        def decode(s:str):
            if s in memo:
                return memo[s]
            if s[0] == "0":
                return 0
            if len(s) == 1:
                return 1
            
            w = decode(s[1::])
            prefix = int(s[:2])
            if prefix <= 26:
                w += decode(s[2::])
                
            memo[s] = w
            
            return w
        
        return decode(s)
