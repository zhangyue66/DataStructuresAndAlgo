class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = ""
        
        cnt = 0
        
        for letter in s:
            if letter == "(":
                cnt += 1
            elif letter == ")" and cnt <=0:
                continue
            elif letter == ")":
                cnt -=1
                
            ans += letter
            
        if cnt > 0:
            res = ""
            cnt = 0
            for letter in ans[::-1]:
                if letter == ")":
                    cnt += 1
                elif letter == "(" and cnt <=0:
                    continue
                elif letter == "(":
                    cnt -= 1
                    
                res += letter
            return res[::-1]
        
        return ans
