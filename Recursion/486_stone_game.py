class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def score(l,r):
            if l == r:
                return nums[l]
            return max(nums[l]-score(l+1,r),nums[r]-score(l,r-1))
        
        return score(0,len(nums)-1) >= 0
