class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ans = 0
        nodes,queue = [],[]
        m,n = len(grid),len(grid[0])
        def check_cur(x,y):
            # this function we use to check cur node's neightbour if they are fresh oranges
            # up down left right
            res = []
            if x - 1 >= 0 and grid[x-1][y] == 1:
                    res.append([x-1,y])
                    
            if x+1 < m and grid[x+1][y] == 1:
                res.append([x+1,y])
                
            if y-1 >= 0 and grid[x][y-1] == 1 :
                res.append((x,y-1))
                
            if y+1 <n and grid[x][y+1] == 1 and [x,y+1]:
                res.append([x,y+1])
            for node in res:
                grid[node[0]][node[1]] = 2
            return res
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    nodes.append([i,j])
        def contain(num):
            for gri in grid:
                if num in gri:
                    return True
            return False
        if not nodes and contain(1):
            return -1
        if 2 in grid and not contain(1):
            return 0
        if not contain(1):
            return 0
        queue.extend(nodes)
        
        while queue:
            #print(queue)
            temp = []
            for k in range(len(queue)):
                cur = queue.pop(0)
                temp.extend(check_cur(cur[0],cur[1]))
            #print(temp) 
            queue = temp
            ans += 1
            #print(queue)
           
        for gri in grid:
            if 1 in gri:
                return -1
        return ans - 1
                
                    
