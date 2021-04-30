class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        if x == 1 and y ==1 and bound >=2:
            return [2]
        if x == 1 and y ==1 and bound <2:
            return []
        
        i,j = 0,0
        
        while x**i <= bound:
            i += 1
            if x == 1:
                break
        while y**j <= bound:
            j += 1
            if y ==1 :
                break
            
        ans = []
        visited = set()
        for a in range(i):
            for b in range(j):
                num = x**a + y**b
                if num in visited:
                    continue
                if  num <= bound:
                    ans.append(num)
                    visited.add(num)
                    
        return ans
