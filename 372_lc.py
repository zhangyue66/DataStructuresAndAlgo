class Solution:
    def superPow(self, a: int, b):

        if len(b) == 0:
            return
        cur = a ** b[0] % 1337
        for i in range(1, len(b)):
            cur = cur ** 10 * a ** b[i] % 1337

        return cur % 1337


yz = Solution()
a =2
b = [1,0,0]
print(yz.superPow(a,b))
