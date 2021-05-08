class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # use recursion method 
        # credit to https://www.youtube.com/watch?v=sSno9rV8Rhg&t=851s
        if not len(text1) or not len(text2):
            return 0
        m,n = len(text1),len(text2)
        def helper(i,j):
            # i represent start of text1 , j represent start of text2
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                return 1+helper(i+1,j+1)
            else:
                return max(helper(i+1,j),helper(i,j+1))
            
        ans = helper(0,0)
        
        return ans
