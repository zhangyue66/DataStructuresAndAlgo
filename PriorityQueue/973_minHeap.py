import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        n = len(points)
        heap = [((abs(points[i][0])**2+abs(points[i][1])**2)**0.5,points[i]) for i in range(n)]
        heapq.heapify(heap)
        ans = []
        while K > 0:
            distance,point = heapq.heappop(heap)
            ans.append(point)
            K -= 1
            
        return ans
