import bisect
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        ans = []
        
        def counting(word):
            target = "z"
            for w in word:
                if w <= target:
                    target = w
            return word.count(target)
        
        q = []
        for query in queries:
            num = counting(query)
            q.append(num)
            
        w = []
        for word in words:
            n = counting(word)
            w.append(n)
        w.sort() 
        #print(q,w)
        for que in q:
            index = bisect.bisect_right(w,que)
            ans.append(len(w)-index)
            
        return ans
            
