class Solution:
    def numberOfSubarrays(self, nums, k):
        lst = [-1]
        for i in range(len(nums)):
            if nums[i] % 2:
                lst.append(i)
        lst.append(len(nums))
        res = 0
        for i in range(1, len(lst) - k):
        # plus the number of windows containing [lst[i], lst[i+k-1]]
            res += (lst[i] - lst[i-1]) * (lst[i+k] - lst[i+k-1])
        return res
