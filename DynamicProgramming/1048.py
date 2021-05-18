
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        n = len(words)
        dp = [1] * n
 
        
        seen = {}
        for i in range(len(words)):
            seen[words[i]] = i
        
        for j in range(len(words)):
            for i in range(len(words[j])):
                # remove current character word[i] and see if word2 in seen
                temp = words[j][:i] + words[j][i+1:]
                if temp in seen:
                    dp[j] = max(dp[j],dp[seen[temp]]+1)
                    
        return max(dp)
                
            
