class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        self.ans = []
        
        def backtrack(start,length,word,s):
            if len(word) == len(s) :
                self.ans.append(word)
                return
            if start == length:
                return 
            
            if s[start].isalpha():
                for charac in [s[start].lower(),s[start].upper()]:
                    #print(charac)
                    word += charac
                    backtrack(start+1,length,word,s)
                    word = word[:-1]
            else:
                word += s[start]
                
                backtrack(start+1,length,word,s)
                word = word[:-1]
                
            
                    
            
            
        backtrack(0,len(S),"",S)
        
        return self.ans
                
                
                
            
