class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        i = 0  # pointer for 0
        j = 0 # pointer for non-zero
        
        n = len(nums)
        
        while i < n:
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
                i += 1
            else:
                i += 1
                
        while j < n:
            nums[j] = 0
            j += 1
            
