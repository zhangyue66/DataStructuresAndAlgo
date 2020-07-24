class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        if R == 0 or C == 0:
            return []
        else:
            bucket = [[] for i in range(R-1+C)]
            for r in range(R):
                for c in range(C):
                    bucket[abs(r-r0)+abs(c-c0)].append([r,c])


            ans = []
            for _ in bucket:
                if _  != []:
                    ans += _

            return ans







yz = Solution()
R = 2
C = 2
r0 = 0
c0 = 1
print(yz.allCellsDistOrder(R,C,r0,c0))
