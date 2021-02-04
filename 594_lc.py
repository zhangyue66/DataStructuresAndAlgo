from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dict = Counter(nums)
        
        ans = 0
        
        for key in dict.keys():
            if key+1 in dict:
                ans = max(ans,dict[key]+dict[key+1])
                
        return ans
