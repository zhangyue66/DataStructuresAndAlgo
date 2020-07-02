class Solution:
    def scoreOfParentheses(self, S):
        stack = []
        res = 0

        for _ in S:
            if _ == "(":
                stack.append(_)
            else:
                if stack[-1] == "(":
                    cur = 1
                    stack.pop()

                else:
                    cur = stack[-1]*2
                    stack.pop()
                    stack.pop()

                while stack and stack[-1] != "(":
                    yz = stack.pop()
                    cur += yz
                stack.append(cur)

        return cur



yz = Solution()
S =  "(())"
print(yz.scoreOfParentheses(S))
