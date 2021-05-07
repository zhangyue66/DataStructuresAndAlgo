class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # dp . top down method
        if len(nums) == 0:
            return False
        n = len(nums)
        dp = [0] * n
        dp[-1] = 1
        
        last = n-1
        for i in range(n-2,-1,-1):
            if i+nums[i] >= last:
                last = i
                dp[i] = 1
                
        return dp[0]
