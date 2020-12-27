class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0 :
            return True
        
        l,r = 0,len(s)-1
        
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            
            if s[l].isnumeric() and s[r].isnumeric():
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
                
            elif s[l].isalpha() and s[r].isalpha():
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            else:
                return False
                
        return True
