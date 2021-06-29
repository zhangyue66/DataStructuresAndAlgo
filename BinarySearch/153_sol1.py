class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        #check if nums are rotated or not
        if nums[-1] > nums[0]:
            return nums[0]
        
        # else do binary search here - nums are rorated 
        # find the lower bound , find Infelction point 
        # [l,r)
        l,r = 0,len(nums)
        while l < r:
            mid = l + (r - l)//2
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid
        if l+1 < len(nums) and nums[l] > nums[l+1]:
            return nums[l+1]
        if nums[l-1] > nums[l]:
            return nums[l]
        return nums[l]
