class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        ans = 0
        for i in range(len(nums)):
            if nums[ans] != nums[i]:
                ans += 1
                nums[ans] = nums[i]
                
        return ans+1
