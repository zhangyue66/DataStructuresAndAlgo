class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        x = 0
        for i in range(1,n+1):
            x ^= nums[i-1]^i
            
            
        return x
        
        
        #a^b^b = a
