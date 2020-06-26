

class Solution:
    def spiralOrder(self, matrix):
        if matrix == []:
            return []
        else:

            res = []

            def rotate(matrix):
                new_matrix = []
                for i in range(len(matrix[0]), 0, -1):
                    new_matrix.append(list(map(lambda x: x[i-1], matrix)))

                return new_matrix

            while len(matrix) != 1:
                yz = matrix.pop(0)
                res.extend(yz)
                matrix = rotate(matrix)

            res.extend(matrix.pop(0))


            return res

yz= Solution()
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]
print(yz.spiralOrder(matrix))
