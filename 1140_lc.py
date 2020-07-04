from functools import lru_cache

class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        cache = [[0 for i in range(n)] for j in range(n+1)]
        @lru_cache()
        def helper(s,M):
            if s >= n:
                return 0
            M = min(M,n)
            if cache[s][M] > 0:
                return cache[s][M]
            if s +2*M >= n:
                cache[s][M] = sum(piles[s:])
                return cache[s][M]
            best = -float("inf")
            curr = 0
            for x in range(1,2*M+1):
                curr += piles[s+x-1]
                best = max(best,curr-helper(s+x,max(x,M)))
            cache[s][M] = best
            return cache[s][M]

        all = sum(piles)
        res = (helper(0,1)+all)//2

        return res


yz = Solution()
piles = [2,7,9,4,4]
print(yz.stoneGameII(piles))
