class Solution:
    def maxProduct(self, words: List[str]) -> int:
        word_dict = {}
        for word in words:
            mask = 0
            for char in word:
                mask |= 1 << (ord(char)-ord("a"))
                
            word_dict[word] = mask
            
        #print(word_dict)
        ans = 0
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if word_dict[words[i]] & word_dict[words[j]] == 0:
                    # meaning no character are in common
                    ans = max(len(words[i])*len(words[j]),ans)
                    
        return ans
        
                
            
