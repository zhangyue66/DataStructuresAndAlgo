class Solution:
    def spiralOrder(self, matrix):
        row,col = len(matrix),len(matrix[0])
        res = []
        check = [[0 for i in range(col)] for j in range(row)] #0 means no checked. if we through it , we change it to 1
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]

        i,j = 0,0
        d = 0
        for _ in range(row*col):
            res.append(matrix[i][j])
            check[i][j] = 1 #browsed,skip next time
            ni,nj = i+dr[d],j+dc[d] #next element
            if 0<= ni < row and 0<= nj < col and check[ni][nj] !=  1:
                i,j = ni,nj
            else:
                d = (d+1)%4
                i,j = i+dr[d],j+dc[d]

        return res


yz= Solution()
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]
print(yz.spiralOrder(matrix))
