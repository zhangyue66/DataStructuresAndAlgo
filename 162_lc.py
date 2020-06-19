class Solution:
    def findPeakElement(self, nums):
        left,right = 0,len(nums)-1

        while left < right:
            mid = (left+right) //2
            if nums[mid] < nums[mid+1]:
                left = mid+1
            else:
                right = mid


        return left

yz = Solution()
nums = [1,2,3,1]
print(yz.findPeakElement(nums))
