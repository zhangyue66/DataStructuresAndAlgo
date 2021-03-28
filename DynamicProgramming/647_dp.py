class Solution:
    def countSubstrings(self, s: str) -> int:
        # if string is palindrom a. single char 2. two chars but both same 3. >2 , s[first] == s[last] and ineer are also palindrom
        
        if not s:
            return 0
        
        cnt = 0 
        
        matrix = [[0 for i in range(len(s))] for j in range(len(s)) ]
        #let diagonize line to be 1 because they are all single char
        
        for i in range(len(s)):
            matrix[i][i] = 1
            cnt += 1
            
        for col in range(1,len(s)):
            for row in range(0,col):
                if row == col-1 and s[col] ==s [row]:
                    matrix[row][col] = 1
                    cnt += 1
                    
                elif matrix[row+1][col-1] == 1 and s[col] == s[row]:
                    matrix[row][col] = 1
                    cnt += 1
                    
        return cnt
