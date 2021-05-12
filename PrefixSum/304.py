class NumMatrix:
    # prefix sum for each row
    def __init__(self, matrix: List[List[int]]):
        m,n = len(matrix),len(matrix[0])
        self.prefixs = []
        for i in range(m):
            prefix,summ=[],0
            for j in range(n):
                summ += matrix[i][j]
                prefix.append(summ)
                
            self.prefixs.append(prefix)
            
        print(self.prefixs)
        
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for row in range(row1,row2+1):
            if col1 -1 >= 0:
                ans += (self.prefixs[row][col2]- self.prefixs[row][col1-1])
            if col1 == 0:
                ans += (self.prefixs[row][col2])
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
