class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0 :
            return
        dp = [0]*len(nums)
        dp[0] = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        
        for i in range(1,len(nums)):
            temp = cur_max
            
            cur_max = max(nums[i],cur_max*nums[i],cur_min*nums[i])
            
            cur_min = min(nums[i],temp*nums[i],cur_min*nums[i])
            
            dp[i] = max(cur_max,cur_min)
            
        return max(dp)
        
