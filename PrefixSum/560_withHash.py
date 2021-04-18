class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # prefix sum with hash table 
        ans = 0
        
        prefix,dict = [],{}
        sum = 0
        for num in nums:
            sum += num
            
            if sum == k:
                ans += 1
                
            
            if sum-k in dict:
                ans += dict[sum-k]
                
                
            if sum not in dict:
                dict[sum] =1
            else:
                dict[sum] += 1
        return ans
