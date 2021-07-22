class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        # scan from left : find curr biggest one
        # scan 2nd time from right: find curr smallest one
        # iterate both left and right,if left[i] <= right[i+1], stop and return 
        n = len(nums)
        left,right = [],[]
        smallest = -float("inf")
        for i in range(n):
            smallest = max(smallest,nums[i])
            left.append(smallest)
        biggest = float("inf")
        for i in range(n-1,-1,-1):
            biggest = min(biggest,nums[i])
            right.append(biggest)
        right = right[::-1]
        print(left,right)   
        for i in range(n-1):
            if left[i] <= right[i+1]:
                return i+1
