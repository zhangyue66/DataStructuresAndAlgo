class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) ==0:
            return []
        
        maps = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans = []
        
        def backtrack(start,end,maps,ans,word,digits):
            if len(word) == len(digits):
                ans.append(word)
                return
            
            for number in maps[digits[start]]:
                word = word + number
                backtrack(start+1,end,maps,ans,word,digits)
                word = word[:-1]
                
        backtrack(0,len(digits),maps,ans,"",digits)
        
        return ans
