class Solution:
    def productExceptSelf(self, nums):
        left,right = [1]*len(nums),[1]*len(nums)
        sum = 1
        for i in range(len(nums)):
            if i == 0:
                continue
            else:
                sum *= nums[i-1]
                left[i] = sum
        yz = 1
        for j in range(len(nums)-1,-1,-1):
            if j == len(nums)-1:
                continue
            else:
                yz *= nums[j+1]
                right[j] = yz

        ans = [1]*len(nums)

        for i in range(len(nums)):
            ans[i] = left[i]*right[i]

        return ans



yz = Solution()
nums = [1,2,3,4]
print(yz.productExceptSelf(nums))
