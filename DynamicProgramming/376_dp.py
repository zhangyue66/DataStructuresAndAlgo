class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        up = [0]*len(nums)
        down = [0]*len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i],down[j]+1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i],up[j]+1)
                    
        return 1+max(down[-1],up[-1])
