class Solution:
    def minOperations(self, n: int) -> int:
        if n == 1:
            return 0
        total = (1+(n-1)*2+1)*n/2
        target = total//n
        cnt = 0
        for i in range(n):
            cnt += abs(2*i+1-target)
        return int(cnt/2)
