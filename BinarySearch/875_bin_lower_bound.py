class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        l,r = 1,max(piles)
        # lower_bound for [l,r) find the first index i such that i can meet time <= H
        while l < r:
            mid = l + (r-l)//2
            time = 0
            for p in piles:
                mod = p%mid
                time += (p//mid)
                if mod:
                    time += 1
            if time <= H:
                r = mid
            else:
                l = mid + 1
        return l
                
