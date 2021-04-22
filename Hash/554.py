class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        for wal in wall:
            if len(wal) > 1:
                for i in range(1,len(wal)):
                    wal[i] += wal[i-1]
                    
                    
        skip = wall[0][-1]
        
        dict = {}
        
        maxx = -float("inf")
        
        for wal in wall:
            for brick in wal:
                if brick != skip :
                    if brick not in dict:
                        dict[brick] =1
                    else:
                        dict[brick] += 1
                    
                    maxx = max(maxx,dict[brick])
                
                
        return len(wall)-maxx if maxx != -float("inf") else len(wall)
                
