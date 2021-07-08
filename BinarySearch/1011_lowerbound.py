class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_cap = max(weights)
        max_cap = sum(weights)
        
        def verify_cap(capacity):
            ans = 0
            ship = 0
            for w in weights:
                if ship + w > capacity:
                    ans += 1
                    ship = w
                elif ship + w == capacity:
                    ans += 1
                    ship = 0
                else:
                    ship += w
            if ship != 0:
                ans += 1
            return ans
        
        l,r = min_cap,max_cap+1
        while l < r:
            mid = l + (r-l)//2
            if verify_cap(mid) <= days:
                r = mid
            else:
                l = mid + 1
        
        return l
                
