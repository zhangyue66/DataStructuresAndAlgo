class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,r = 1,n+1
        while l < r:
            mid = l + (r - l)//2
            if isBadVersion(mid) is True:
                r = mid
            else:
                l = mid + 1
        return l
