from collections import defaultdict
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        nums = defaultdict(list)
        visited = set()
        for i,w in enumerate(wordsDict):
            nums[w].append(i) 
        #print(nums)
        l1,l2 = nums[word1],nums[word2]
        n1,n2 =len(l1),len(l2)
        i,j = 0,0
        ans = float("inf")
        if word1 == word2:
            for k in range(1,len(l1)):
                ans = min(ans,l1[k]-l1[k-1])
            return ans

        while i < n1 and j < n2:
            ans = min(ans,abs(l1[i]-l2[j]))
            if l1[i] < l2[j]:
                i += 1
            else:
                j += 1          
        return ans
