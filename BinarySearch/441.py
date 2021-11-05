class Solution:
    def arrangeCoins(self, n: int) -> int:
        left,right = 1,n+1
        while left < right:
            mid = (right - left ) // 2 + left
            total = (1+mid)*(mid)//2
            if total == n:
                return mid
            elif total > n:
                right = mid
            else:
                left = mid+1
        return left-1
