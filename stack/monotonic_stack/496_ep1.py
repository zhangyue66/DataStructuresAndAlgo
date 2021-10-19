class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #this is using monotonic_min_stack
        maps = {}
        ans = []
        stack = []
        for num2 in nums2:
            while stack and stack[-1] < num2:
                cur = stack.pop()
                maps[cur] = num2
            stack.append(num2)
        while stack:
            cur = stack.pop()
            maps[cur] = -1
        for num1 in nums1:
            ans.append(maps[num1])
        return ans
