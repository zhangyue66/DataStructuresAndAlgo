class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float("inf")]*len(nums)
        dp[n-1] = 0
        
        for i in range(n-2,-1,-1):
            
            step = float("inf")
            end = min(n-1,i + nums[i])+1
            #print("i is %d, end is %d"%(i,end))
            for j in range(i+1,end):
                
                step = min(step,dp[j])
                #print(step)
                
                
            if step != float("inf"):
                dp[i] = step + 1
            
        return dp[0]
