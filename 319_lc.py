class Solution:
    def bulbSwitch(self, n):
        bulb = [1]*(n+1)
        for i in range(1,n+1):
            if i == 1:
                continue
            else:
                for j in range(1,n+1):
                    if j % i == 0:
                        if bulb[j] == 0:
                            bulb[j] = 1
                        else:
                            bulb[j] = 0

        return bulb.count(1)-1

yz = Solution()
n = 36
print(yz.bulbSwitch(n))
