class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # greedy find all highs and lows in nums 
        
        ans = 1
        k = -2
        for i in range(1,len(nums)):
            k_prev = k
            if nums[i] > nums[i-1]:
                k = 1
            elif nums[i] < nums[i-1]:
                k = -1
            else:
                k = k_prev
                
            if k != k_prev:
                ans += 1

        return ans
