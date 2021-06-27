class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        l,r = 0,n
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] >= n-mid:
                if mid == 0 or nums[mid-1] < n-mid:#correct index
                    return n-mid
                else:
                    r = mid
            else:
                l = mid + 1
        return -1
        
