class Solution:
    def countNumbersWithUniqueDigits(self, n):
        self.duplicate = []

        def helper(n):


            for i in range(10**n):
                visited = []

                for num in str(i):
                    if num in visited:
                        self.duplicate.append(i)
                        break
                    else:
                        visited.append(num)





        helper(n)

        return 10**n-len(self.duplicate)





yz = Solution()
n = 2
print(yz.countNumbersWithUniqueDigits(n))
