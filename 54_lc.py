class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        #col = len(matrix[0])
        
        if row == 0:
            return []
        
        ans = []
        
        colBegin = 0
        colEnd = len(matrix[0])-1
        rowBegin = 0
        rowEnd = len(matrix) -1
        
        
        
        while rowBegin <= rowEnd and colBegin <= colEnd :
            for j in range(colBegin,colEnd+1):
                ans.append(matrix[rowBegin][j])
                
            rowBegin += 1
            
            for i in range(rowBegin,rowEnd+1):
                ans.append(matrix[i][colEnd])
                
            colEnd -= 1
            
            if rowBegin <= rowEnd :
                for j in range(colEnd,colBegin-1,-1):
                    ans.append(matrix[rowEnd][j])

                rowEnd -= 1
            if colBegin <= colEnd:
                for i in range(rowEnd,rowBegin-1,-1):
                    ans.append(matrix[i][colBegin])

                colBegin += 1
            
            #print("rb,re,cb,ce" ,rowBegin,rowEnd,colBegin,colEnd)
            
            
        return ans
