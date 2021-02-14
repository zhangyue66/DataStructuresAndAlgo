class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        
        visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    visited[i][j] = True
        # up,upright,right,downright,down,downleft,left,upleft            
        directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
        queue = [(0,0,1)] # x,y,distance
        visited[0][0] = True
        
        while queue:
            x,y,dist = queue.pop(0)
            #print(x,y)
            if x==len(grid)-1 and y == len(grid[0])-1:
                return dist
            
            for dx,dy in directions:
                if 0 <= x+dx <= len(grid)-1 and 0 <= y+dy <= len(grid[0])-1:
                    if visited[x+dx][y+dy] is False:
                        queue.append((x+dx,y+dy,dist+1))
                        visited[x+dx][y+dy] = True
                        
                        
                        
        return -1
        #https://www.geeksforgeeks.org/shortest-distance-two-cells-matrix-grid/
            
