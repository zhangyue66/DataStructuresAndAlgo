class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1 for i in range(n)] for j in range(n)]
        for mine in mines:
            grid[mine[0]][mine[1]] = 0
        def helper():
            ans = [[0 for i in range(n)] for j in range(n)]
            return ans
        left,right,up,down = helper(),helper(),helper(),helper()
        #left
        for i in range(n):
            temp_sum = 0
            for j in range(n):
                if grid[i][j] != 0:
                    temp_sum += 1
                    left[i][j] = temp_sum
                else:
                    temp_sum = 0
                    left[i][j] = 0
        #right
        for i in range(n):
            temp_sum = 0
            for j in range(n-1,-1,-1):
                if grid[i][j] != 0:
                    temp_sum += 1
                    right[i][j] = temp_sum
                else:
                    temp_sum = 0
                    right[i][j] = 0
        #up
        for x in range(n):
            temp = 0
            for y in range(n):
                if grid[y][x] != 0:
                    temp += 1
                    up[y][x] = temp
                else:
                    temp = 0
                    up[y][x] = 0
        #down
        for x in range(n):
            temp = 0
            for y in range(n-1,-1,-1):
                if grid[y][x] != 0:
                    temp += 1
                    down[y][x] = temp
                else:
                    temp = 0
                    down[y][x] = 0
        res = 0
        for i in range(n):
            for j in range(n):
                degree = min(left[i][j],right[i][j],up[i][j],down[i][j])
                res = max(degree,res)
        return res
