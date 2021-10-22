import heapq
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        # use max heapq
        heap = []
        maps = Counter(s)
        for k,v in maps.items():
            heapq.heappush(heap,(-v,k))
        ans = ""
        while heap:
            cnt,char = heapq.heappop(heap)
            ans += (-cnt*char)
        return ans
