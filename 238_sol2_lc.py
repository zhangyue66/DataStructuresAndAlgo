class Solution:
    def productExceptSelf(self, nums):
        ans = [1]*len(nums)
        sum = 1
        for i in range(1,len(nums)):
            sum *= nums[i-1]
            ans[i] = sum



        j = len(nums)-1
        right = 1
        while j >= 0:
            if j == len(nums)-1:
                j -= 1
            else:
                right *= nums[j+1]
                ans[j] = right*ans[j]
                j -= 1


        return ans



yz = Solution()
nums = [1,2,3,4]
print(yz.productExceptSelf(nums))
