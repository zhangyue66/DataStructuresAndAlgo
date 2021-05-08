class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # use recursion method 
        # credit to https://www.youtube.com/watch?v=sSno9rV8Rhg&t=851s
        if not len(text1) or not len(text2):
            return 0
        
        # enhance with memorization Time Complex: O(m*n)
        m,n = len(text1),len(text2)
        memo = [[ -1 for j in range(n+1)] for i in range(m+1)]
        #print(memo)
        def helper(i,j):
            # i represent start of text1 , j represent start of text2
            if memo[i][j] != -1:
                return memo[i][j]
            if i == m or j == n:
                memo[i][j] = 0
                return 0
            if text1[i] == text2[j]:
                ans = 1+helper(i+1,j+1)
                memo[i][j] = ans
                return ans
            else:
                ans = max(helper(i+1,j),helper(i,j+1))
                memo[i][j] = ans
                return ans
            
        ans = helper(0,0)
        
        return ans
