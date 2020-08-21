
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        dict = {}
        left ={}
        right = {}
        degree = 1
        
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] =1
                left[nums[i]] = i
                right[nums[i]] = i
            else:
                dict[nums[i]] += 1
                degree = max(dict[nums[i]],degree)
                right[nums[i]] = i
        ans = float("inf")        
        for k,v in dict.items():
            if v == degree:
                ans = min(ans,right[k]-left[k]+1)
                
        return ans
                
