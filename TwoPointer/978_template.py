class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        ans = 1
        n = len(arr)
        start,end = 0,0
        def helper(index):
            if arr[index] > arr[index-1] and arr[index] > arr[index+1]:
                return True
            if arr[index] < arr[index-1] and arr[index] < arr[index+1]:
                return True
            return False
        
        while start < n-1:
            if arr[start] == arr[start+1]:
                start += 1
                continue
            end = start + 1
            while end < n-1 and helper(end):
                end += 1
            ans = max(ans,end-start+1)
            start = end
        return ans
