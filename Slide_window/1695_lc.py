class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        sum_val = 0
        #sliding window [i,j]
        
        seen = set()
        
        i = 0
        
        for j in range(len(nums)):
            while nums[j] in seen:
                sum_val -= nums[i]
                
                seen.remove(nums[i])
                
                i += 1
                
            seen.add(nums[j])
            sum_val += nums[j]
            ans = max(sum_val,ans)
            
        return ans
