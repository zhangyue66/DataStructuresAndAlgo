class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1,1]
        while fib[-1] < k:
            num = fib[-1] + fib[-2]
            fib.append(num)

        #     return fib
        # [1, 1, 2, 3, 5, 8]

        if fib[-1] == k :
            return 1
        fib.pop() # dont need the last element
        ans = 0

        for num in fib[::-1]:
            if k >= num :
                ans += 1
                k -= num

        return ans
