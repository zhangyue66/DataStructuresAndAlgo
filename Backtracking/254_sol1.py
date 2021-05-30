# Numbers can be regarded as the product of their factors.

#     For example, 8 = 2 x 2 x 2 = 2 x 4.

# Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

# Note that the factors should be in the range [2, n - 1].


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n < 2:
            return []
        
        factors = []
        for i in range(2,n):
            if n % i == 0:
                factors.append(i)
        
        # get all factors and start combination
        
        ans = []
        visited = set()
        def backtrack(comb,target,factors,start):
            if target < 1:
                return
            if target == 1:
                ans.append(comb[:])
                return
            for start in range(start,len(factors)):
                comb.append(factors[start])
                backtrack(comb,target/factors[start],factors,start)
                comb.pop()

        backtrack([],n,factors,0)
        
        return ans
        
