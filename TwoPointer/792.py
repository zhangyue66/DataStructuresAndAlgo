class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        def check_sub(word1,word2):
            m,n = len(word2),len(word1)
            fast,slow = 0,0 #word2 , word1
            while fast < m:
                if word2[fast] == word1[slow]:
                    slow += 1
                    if slow == n:
                        return True
                fast += 1  
            if slow == n:
                return True
            return False
        mapping = set()
        visited = set()
        for word in words:
            if word in mapping:
                ans += 1
            elif word in visited:
                continue
            else:
                if check_sub(word,s):
                    mapping.add(word)
                    
                    ans += 1
                else:
                    visited.add(word)
                
        return ans
            
            
            
