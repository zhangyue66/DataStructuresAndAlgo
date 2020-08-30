class Solution:
    def setZeroes(self, matrix):
        row_set = set()
        column_set = set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if j not in row_set:
                        row_set.add(j)
                    if i not in column_set:
                        column_set.add(i)

        if len(row_set) != 0:
            for row in row_set:
                for i in range(len(matrix)):
                    for j in range(len(matrix[0])):
                        if j == row:
                            matrix[i][j] = 0
        if len(column_set) != 0:
            for col in column_set:
                for i in range(len(matrix)):
                    for j in range(len(matrix[0])):
                        if i == col:
                            matrix[i][j] = 0

        return matrix



yz = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(yz.setZeroes(matrix))
