class Solution:
    def baseNeg2(self, N):
        if N == 0:
            return "0"
        else:
            res = []
            while N:
                res.append(N&1)
                N = -(N>>1)
            return "".join(str(e) for e in res[::-1])



yz = Solution()
N = 4
print(yz.baseNeg2(N))
