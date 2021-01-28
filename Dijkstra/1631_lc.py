import heapq
from collections import defaultdict

class Solution(object):
    def minimumEffortPath(self, heights):
        r,c = len(heights),len(heights[0])
        distance = [[float("inf") for i in range(c)] for j in range(r)]
        minHeap =[(0,0,0)] # distance,row,column
        directions = [[-1,0],[1,0],[0,-1],[0,1]] #up,down,left,right

        while minHeap:
            dis,row,col = heapq.heappop(minHeap)
            if dis > distance[row][col]:
                continue
            if row == r-1 and col == c-1:
                print(distance)
                return dis  # already reached bottom right (r-1,c-1)

            #now start to calucate the cost for the 4 connected edges
            for i in range(4):
                #print(directions[i][0])
                nr,nc = row+directions[i][0],col+directions[i][1]
                if 0<=nr<r and 0<= nc < c:
                    new_dis = max(dis,abs(heights[nr][nc]-heights[row][col]))
                    if distance[nr][nc] > new_dis:
                        distance[nr][nc] = new_dis
                        heapq.heappush(minHeap,(new_dis,nr,nc))

heights = [[1,2,2],[3,8,2],[5,3,5]]
yz = Solution()
print(yz.minimumEffortPath(heights))
