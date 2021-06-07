
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        nums = set(nums)
        for k in nums:
            if k-1 not in nums:
                length = 0
                while k in nums:
                    length += 1
                    
                    k += 1
                ans = max(ans,length)
                    
        return ans
