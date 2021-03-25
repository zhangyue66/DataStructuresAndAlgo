class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
      #Credit to HuaHua
        if not matrix:
            return []
        def dfs(matrix,x,y,h):
            if x < 0 or y < 0: #reaching pacific
                return 1
            if x == len(matrix[0]) or y == len(matrix): # reaching atlantic
                return 2
            if matrix[y][x] > h:
                return 0
            #direction = ((1,0),(-1,0),(0,1),(0,-1))
            height = matrix[y][x]
            matrix[y][x] = float("inf")  # why we need this ? if we dont have this , recursion stack reach maximum
            valid = dfs(matrix,x+1,y,height) | dfs(matrix,x-1,y,height) | dfs(matrix,x,y+1,height) | dfs(matrix,x,y-1,height)
            
            
            matrix[y][x] = height
            
            return valid
        
        ans = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if dfs(matrix,j,i,matrix[i][j]) ==3:
                    ans.append([i,j])
                    
        return ans
    

            
            
        
