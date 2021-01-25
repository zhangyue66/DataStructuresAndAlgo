from collections import defaultdict
class Solution:
    def diagonalSort(self, mat):
        m,n = len(mat),len(mat[0])
        dict = defaultdict(list)

        for i in range(m):
            for j in range(n):
                dict[i-j].append(mat[i][j])

        for k,v in dict.items():
            v.sort(reverse=True)

        for i in range(m):
            for j in range(n):
                mat[i][j] = dict[i-j].pop()

        return mat
