class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 1
        small , big = float("inf"),-float("inf")
        cnt = 0
        
        for i in range(len(nums)):
            if nums[i] > 0:
                small = min(small,nums[i])
                big = max(big,nums[i])
                cnt += 1
                
        if small > 1:
            return 1
        else:
            # a number between (small:big) must be missing 
            for j in range(small,big):
                if j not in nums:
                    return j
            
            return big+1
