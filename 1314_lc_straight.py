    def matrixBlockSum(self, mat, K: int):
        r,c = len(mat),len(mat[0])
        res = [[0 for i in range(c)] for j in range(r)]

        for i in range(r):
            for j in range(c):
                sum = 0
                #row,col = 0,0

                #while 0<=row<r and 0 <=col <c and  i-K<=row<=i+K and j-K<=col<=j+K:
                for row in range(max(0,i-K),min(r,i+K+1)):
                    for col in range(max(0,j-K),min(c,j+K+1)):
                        sum+= mat[row][col]

                res[i][j] = sum


        return res
        
       
yz = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
K = 2
print(yz.matrixBlockSum(mat,K))
