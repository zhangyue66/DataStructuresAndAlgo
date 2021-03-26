class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        
        pacific_visited = set()
        atlantic_visited = set()
        directions = ((0,1),(0,-1),(1,0),(-1,0))
        
        # idea is from Pacific or Atlantic, which node we can reach 
        def dfs(i,j,visited,matrix):
            if (i,j) in visited:
                return
            
            visited.add((i,j))
            
            for x,y in directions:
                if 0 <=i+x <len(matrix) and 0 <=j+y< len(matrix[0]):
                    if matrix[i+x][j+y] >= matrix[i][j]:
                        dfs(i+x,j+y,visited,matrix)
                        
        for row in range(len(matrix)):
            dfs(row,0,pacific_visited,matrix)
            dfs(row,len(matrix[0])-1,atlantic_visited,matrix)
            
        for col in range(len(matrix[0])):
            dfs(0,col,pacific_visited,matrix)
            dfs(len(matrix)-1,col,atlantic_visited,matrix)
            
        return atlantic_visited.intersection(pacific_visited)
            
