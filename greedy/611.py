class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # credit to Huahua https://www.youtube.com/watch?v=bojX9bdra-w
        n = len(nums)
        nums.sort(reverse=True)
        if n < 3:
            return 0
        ans = 0
        
        for i in range(n-2):
            j,k = i+1,n-1
            while j < k:
                if nums[j] + nums[k] > nums[i]:
                    ans += (k-j)
                    j += 1
                else:
                    k -= 1
        return ans
