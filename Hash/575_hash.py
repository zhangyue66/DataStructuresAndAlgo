import collections
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        dict = collections.Counter(candyType)
        ans = min(len(dict.keys()),len(candyType)//2)
        
        return ans
