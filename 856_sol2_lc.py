class Solution:
    def scoreOfParentheses(self, S):


        def helper(l,r,S):
            if r - l == 1:
                return 1
            else:
                balanced = 0
                for i in range(l,r):

                    if S[i] == "(":
                        balanced += 1
                    if S[i] == ")":
                        balanced -= 1
                    if balanced == 0:
                        return helper(l,i,S)+helper(i+1,r,S)

                return 2*helper(l+1,r-1,S)


        res = helper(0,len(S)-1,S)

        return res




yz = Solution()
S =  "()(())"
print(yz.scoreOfParentheses(S))
