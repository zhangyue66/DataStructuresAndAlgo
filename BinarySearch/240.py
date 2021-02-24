class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # search from top-right corner
        
        col,row = len(matrix),len(matrix[0])
        
        i,j = 0,row-1
        
        while i < col and j >=0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
               i += 1
                
        return False
