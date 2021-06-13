import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # use min heap , first calculate the smallest ratio , each time pop out the smallest ration one
        n = len(classes)
        heap = [(-((classes[i][0]+1)/(classes[i][1]+1)-(classes[i][0])/(classes[i][1])),classes[i][0],classes[i][1]) for i in range(n)]
        heapq.heapify(heap)
        #print(heap) 
        while extraStudents > 0:
            ratio,pas,total = heapq.heappop(heap)
            pas += 1
            total += 1
            ratio = -((pas+1)/(total+1) - (pas/total))
            heapq.heappush(heap,(ratio,pas,total))
            extraStudents -= 1
            
        ans = 0
        for item in heap:
            ans += (item[1]/item[2])
        #print(heap,pass_total,sum_total)
        return ans / len(heap)
