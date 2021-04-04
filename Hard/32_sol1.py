class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # credit to https://www.youtube.com/watch?v=VdQuwtEd10M
        stack = [-1]
        ans = 0
        for i in range(len(s)):
            if s[i] == ")":
                stack.pop()
                if not stack:
                    # if stack is empty, need to push cur index
                    stack.append(i)
                else:
                    ans = max(ans,i-stack[-1])
            else:
                
                #if open bracket "("
                stack.append(i)
            
        return ans
