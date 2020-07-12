class Solution:
    def findBestValue(self, arr, target):
        if sum(arr) <= target or max(arr) * len(arr) < target:
            return max(arr)
        else:
            n = len(arr)
            arr.sort(reverse=True)
            while arr and target >= arr[-1]*len(arr):
                target -= arr.pop()

            if target / len(arr) - target//len(arr) <= 0.5:
                return target //len(arr)
            return target // len(arr) + 1

yz = Solution()
arr = [1,2,23,24,34,36]
target = 110
print(yz.findBestValue(arr,target))
