import re
class Solution:
    def myAtoi(self, s: str) -> int:
        minNum = -2**31
        maxNum = 2**31-1
        
        #pattern = r"[\-\+]?\d+?"
        
        pattern = r"^[-+]?\d+"
        s = s.strip()
        digits = re.search(pattern,s)
        
        if digits:
            nums = digits.group()
            if ("-" in nums or "+" in nums) and len(nums) == 1:
                
                return 0
            else:
                ans = int(nums)
                
                if ans > maxNum:
                    return maxNum
                if ans < minNum:
                    return minNum
                
                return ans
        return 0
        
