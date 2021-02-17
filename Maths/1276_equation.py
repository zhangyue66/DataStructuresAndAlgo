class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        #ans = []
        jumbo,small = 0,0
        
        if tomatoSlices-2*cheeseSlices<0:
            return []
        if (tomatoSlices-2*cheeseSlices)%2 != 0:
            return []
        
        jumbo = (tomatoSlices-2*cheeseSlices) // 2
        small = cheeseSlices-jumbo
        
        if small <0:
            return []
        
        return [jumbo,small]
