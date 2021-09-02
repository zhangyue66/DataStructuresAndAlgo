class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ans = 0
        seen =[0]*len(nums)
        for num in nums:
            cnt = 0
            while seen[num] == 0:
                seen[num],cnt,num = 1,cnt+1,nums[num]
            ans = max(ans,cnt)
        return ans
