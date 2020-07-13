class Solution:
    def countSquares(self, matrix):
        col,row = len(matrix),len(matrix[0])
        if col ==0 or row == 0 :
            return 0
        else:

            cnt = 0

            for i in range(col):
                for j in range(row):
                    if matrix[i][j] == 0:
                        continue
                    if i ==0 or j == 0:
                        cnt += 1
                        continue

                    mini = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])

                    matrix[i][j] += mini
                    cnt += matrix[i][j]

            return cnt



yz = Solution()
matrix = \
    [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
    ]
print(yz.countSquares(matrix))
