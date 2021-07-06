import heapq
from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        d = Counter(arr)
        heap = []
        for _,v in d.items():
            heapq.heappush(heap,-v)
        
        ans = 0
        cnt = 0
        
        while cnt < n/2:
            #val = -heapq.heappop(heap)
            cnt += (-heapq.heappop(heap))
            ans += 1
            
        return ans
            
