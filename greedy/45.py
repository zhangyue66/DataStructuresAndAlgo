class Solution:
    def jump(self, nums: List[int]) -> int:
        # use Greedy O(N) method
        begin,end,fatherest=0,0,0
        ans = 0
        
        for i in range(len(nums)-1):
            fatherest = max(fatherest,i + nums[i])
            if i == end:
                ans += 1
                end = fatherest
                
        return ans
