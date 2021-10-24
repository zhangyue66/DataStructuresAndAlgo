class Solution:
    def findMin(self, nums: List[int]) -> int:
        # arr = arr + arr copy arr 1 time so there is searching space 
        # if nums[0] < nums[-1]
        if nums[0] >= nums[-1]:
            nums.extend(nums)
            lb,rb = 0,0
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    lb = i+1
                    break
            for j in range(len(nums)-1,0,-1):
                if nums[j] < nums[j-1]:
                    rb = j-1
                    break
            l,r = lb,rb
            return nums[lb]
        else:
            return nums[0]
