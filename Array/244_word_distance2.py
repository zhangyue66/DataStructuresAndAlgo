from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.visited = {}
        self.nums = defaultdict(list)
        for i,w in enumerate(wordsDict):
            self.nums[w].append(i)
        
        

    def shortest(self, word1: str, word2: str) -> int:
        if (word1,word2) in self.visited:
            return self.visited[(word1,word2)]
        l1,l2 = self.nums[word1],self.nums[word2]
        ans = float("inf")
        for i in range(len(l1)):
            for j in range(len(l2)):
                ans = min(ans,abs(l1[i]-l2[j]))
        self.visited[(word1,word2)] = ans
        return ans
                
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
