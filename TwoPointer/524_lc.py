class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        if not d:
            return ""
        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            i = 0
            for letter in s:
                if i < len(word) and word[i] == letter:
                    i+=1
                    
            if i == len(word):
                return word
        return ""
