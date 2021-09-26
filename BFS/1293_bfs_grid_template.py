class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        # use BFS(x,y,remain)
        #directions [up,down,left,right]
        directions = [[-1,0],[1,0],[0,-1],[0,1]]
        m,n = len(grid),len(grid[0])
        queue = [[0,0,k]]
        visited = set()
        #visited.add((0,0,k))
        step = 0
        while queue:
            size = len(queue)
            #print(size)
            while size != 0:
                cur = queue.pop(0)
                size -= 1
                if cur[0] == m-1 and cur[1] == n-1:
                    return step
                for d in directions:
                    i,j = cur[0]+d[0],cur[1]+d[1]
                    obs = cur[2]
                    if 0<=i<m and 0<=j<n:
                        if grid[i][j] == 0 and (i,j,obs) not in visited:
                            visited.add((i,j,obs))
                            queue.append([i,j,obs])
                        elif grid[i][j] == 1 and obs > 0 and (i,j,obs-1) not in visited:
                            queue.append([i,j,obs-1])
                            visited.add((i,j,obs-1))
            step += 1
            
        return -1
