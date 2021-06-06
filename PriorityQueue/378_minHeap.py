import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for row in matrix:
            heap += row
            
        heapq.heapify(heap)
        while k > 0:
            cur = heapq.heappop(heap)
            k -= 1
        return cur
            
            
        
