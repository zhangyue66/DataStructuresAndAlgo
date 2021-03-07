class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        ans = ""
        
        words = sorted(words,key=lambda x : len(x),reverse=True)
        #print(words)
        comp = []
        
        for word in words:
            if not ans:
                ans += (word+"#")
                comp.append(word)
            else:
                is_found = False
                for string in comp:
                    if word in string and string[-(len(word))::] == word:
                        is_found = True
                        break
                if not is_found:
                    ans += (word+"#")
                    comp.append(word)
        #print(ans)
        return len(ans)
