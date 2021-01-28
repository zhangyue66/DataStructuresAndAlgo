import numpy
class Solution:
    def concatenatedBinary(self, n: int) -> int:
    #idea is to shift digits . every time for n , shift digits = 1+log2(i) so answer is  ans << digits + i
        ans = 0
        i = 1
        while i <= n:
            ans = ((ans<<(1+int(numpy.log2(i)))%(10**9+7)) + i)

            i += 1

        return ans%(10**9+7)

yz = Solution()
print(yz.concatenatedBinary(n=63556))
