import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # use min heap to track all the biggest step for now
        heap = []
        for i in range(1,len(heights)):
            delta = heights[i]- heights[i-1]
            if delta <= 0:
                continue
            else:
                if len(heap) < ladders:
                    heapq.heappush(heap,delta)
                    
                else:
                    if len(heap) !=0  and heap[0] <= delta:
                        bricks -= heapq.heappop(heap)
                        heapq.heappush(heap,delta)
                    else:
                        bricks -= delta
                    if bricks < 0:
                            return i-1
                        
        return len(heights)-1
