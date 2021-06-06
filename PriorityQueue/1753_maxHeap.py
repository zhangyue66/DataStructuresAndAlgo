import heapq
class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        score = 0
        heap = [-a,-b,-c]
        heapq.heapify(heap)
        while len(heap) >= 2:
            biggest = heapq.heappop(heap)
            bigger = heapq.heappop(heap)
            biggest += 1
            bigger += 1
            if biggest < 0:
                heapq.heappush(heap,biggest)
            if bigger < 0:
                heapq.heappush(heap,bigger)
                
            score += 1
            
        return score
        
