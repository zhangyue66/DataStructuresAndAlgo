class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        # use monotone stack - always store biggest value in stack
        n = len(temperatures)
        stack = []
        ans = [0]*n
        
        for i,t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                cur = stack.pop() # index
                day = i - cur
                ans[cur] = day
            stack.append(i)
        return ans
