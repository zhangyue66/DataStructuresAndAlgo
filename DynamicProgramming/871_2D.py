class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # brute force to solve 
        n = len(stations)
        dp = [startFuel] * (n+1)
        
        for i in range(n):
            for j in range(i,-1,-1):
                if dp[j] >= stations[i][0]:
                    dp[j+1] = max(dp[j+1],dp[j] + stations[i][1])
                    
        for i in range(n+1):
            if dp[i] >= target:
                return i
        #print(dp)    
        return -1
            
