class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[-1] > nums[0]:
            return nums[0]
        l,r = 0,n-1
        while l < r:
            # find the lower_bound element which > nums[0]
            mid = (r-l)//2 + l
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
