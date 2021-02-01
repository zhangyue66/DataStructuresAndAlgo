class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        i,j = len(nums)-1,len(nums)-2
        
        while j >= 0:
            if nums[i] <= nums[j]:
                i -=1
                j -=1
            else:
                break
                
        if j == -1:# means descending sequence. not possible answer
            nums.reverse()
            return 
        
        i = len(nums)-1
        index = j
        while i > j:
            if nums[i] <= nums[j]:
                i -= 1
            else:
                nums[i],nums[j] = nums[j],nums[i]
                break
        #print("yz")  
        l,r = j+1,len(nums)-1
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
