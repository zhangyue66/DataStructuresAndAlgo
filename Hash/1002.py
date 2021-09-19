class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0])
        res = Counter(words[0])
        for word in words[1:]:
            res = res & Counter(word)
            
        return list(res.elements())
