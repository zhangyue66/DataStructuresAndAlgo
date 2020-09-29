class Solution:
    def letterCasePermutation(self, S):
        self.ans = []

        def backtrack(res,start):
            if len(res) == len(S):
                self.ans.append(res)
                return
            if S[start].isalpha():
                yz = [S[start].upper(),S[start].lower()]
                for letter in yz:
                    backtrack(letter+res,start+1)

            else:
                backtrack(S[start]+res,start+1)


        backtrack("",0)

        return self.ans


yz = Solution()
S = "a1b2"
print(yz.letterCasePermutation(S))
