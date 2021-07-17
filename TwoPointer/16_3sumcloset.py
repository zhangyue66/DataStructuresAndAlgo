class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        gap = float("inf") # find the smallest gap for now using abs()
        n = len(nums)
        ans = 0
        #print(nums)
        for i in range(n-2):
            j,k = i+1,n-1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if abs(target-summ) < abs(gap):
                    gap = target - summ
                    ans = summ
                if summ < target:
                    j += 1
                else:
                    k -= 1
                
                if gap == 0:
                    break
        return ans
