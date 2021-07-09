"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        for x in range(1,1001):
            l,r = 1,1000
            while l <= r:
                mid = l + (r-l)//2
                if customfunction.f(x,mid) == z:
                    ans.append([x,mid])
                    break
                elif customfunction.f(x,mid) < z:
                    l = mid + 1
                else:
                    r = mid - 1
            
                    
        return ans
        
