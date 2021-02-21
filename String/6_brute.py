class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        directions = [(1,0),(-1,1)]
        
        matrix = [["" for i in range(len(s))] for j in range(numRows)]
        
        i,j = 0,0
        k=0
        while k <= len(s)-1:
            for dx,dy in directions:
                for step in range(numRows-1):
                    if k <= len(s)-1:
                        matrix[i][j] = s[k]
                    i += dx
                    j += dy
                    k += 1
        ans = ""        
        for col in matrix:
            ans += "".join(col)
        #print(matrix)    
        return ans
            
