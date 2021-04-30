import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        
        i = bisect.bisect_left(nums,target)
        if i == len(nums) or nums[i] != target:
            return [-1,-1]
                
        left = bisect.bisect_left(nums,target)
        
        right = bisect.bisect_right(nums,target)
        
        return [left,right-1]
