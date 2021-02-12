class Solution:
    def maximumSwap(self, num: int) -> int:
        #2996
        #9926 
        
        nums =[int(i) for i in str(num)]
        
        max_idx = len(nums)-1
        
        l,r = 0,0
        
        for i in range(len(nums)-1,-1,-1):
            if nums[i] > nums[max_idx]:
                max_idx = i
                
            elif nums[i] < nums[max_idx]:
                l = i
                r = max_idx
                
        nums[l],nums[r] = nums[r],nums[l]
        
        return int("".join([str(i) for i in nums]))
