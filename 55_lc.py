class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) ==0:
            return False
        farthest = 0
        
        for i in range(len(nums)):
            if i > farthest:
                return False
            farthest = max(nums[i]+i,farthest)
        
        return farthest >= len(nums)-1
