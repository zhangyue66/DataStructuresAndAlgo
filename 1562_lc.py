class Solution:
    def findLatestStep(self, A, m: int):
        if m == len(A): return m
        length = [0] * (len(A) + 2)
        res = -1
        for i, a in enumerate(A):
            left, right = length[a - 1], length[a + 1]
            if left == m or right == m:
                res = i
            length[a - left] = length[a + right] = left + right + 1
        return res



yz = Solution()
A = [3,5,1,2,4]
m = 1
print(yz.findLatestStep(A,m))
