class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # sort() first, 0 to mid all increase
        # mid or mid + 1 to last element all decrease
        nums.sort()
        if len(nums) == 1:
            return 0
        step = 0
        # find median number
        #if it is even median = (mid + mid-1) // 2
        # if it is odd median = mid
        
        n = len(nums)
        mid = n // 2
        if n % 2 == 0:
            median = (nums[mid] + nums[(mid-1)]) // 2
            
        else:
            median = nums[mid]
            
        for num in nums:
            step += abs(num - median)
            
        return step 
