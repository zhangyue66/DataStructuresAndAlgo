class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l < r:
            mid = l+(r-l)//2
            if mid % 2 == 0:
                check = mid + 1
            else:
                check = mid - 1
            
            if nums[mid] == nums[check]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
