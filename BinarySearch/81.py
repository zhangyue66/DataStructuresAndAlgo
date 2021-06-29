class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0,len(nums)-1
        
        while l <= r:
            mid = l + (r - l)//2
            if nums[mid] == target:
                return True
            
            if nums[mid] == nums[l]:
                l += 1
            elif nums[mid] == nums[r]:
                r -= 1
            elif nums[mid] > nums[l]:# i can deploy BS in this side - search space
                if target >= nums[l] and target <= nums[mid]:
                    r = mid 
                else:
                    l = mid 
            elif nums[mid] < nums[r]:
                if nums[mid] <= target and target <= nums[r]:
                    l = mid 
                else:
                    r = mid
        
        # returning l
        # if nums[l] == target or nums[r] == target:
        #     return True
        return False
                
                
                
        
