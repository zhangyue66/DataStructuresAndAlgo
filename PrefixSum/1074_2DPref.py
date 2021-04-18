class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # first use prefix sum on row - convert matrix
        m,n = len(matrix),len(matrix[0])
        
        for i in range(m):
            for j in range(1,n):
                matrix[i][j] += matrix[i][j-1]
        #print(matrix)       
        # use the Hash method in Leetcode#560 
        # iterate on Column C1 and C2 , with row changing from 1 - end. O(N^2*M)
        # sum - target in Hash or not 
        count = 0
        for c1 in range(n):
            for c2 in range(c1,n):
                dict = {0:1}
                summ = 0           
                for row in range(m):
                    if c1==0:
                        summ += matrix[row][c2]
                    else:
                        summ += (matrix[row][c2]-matrix[row][c1-1])
                    
                    if summ - target in dict:
                        count += dict[summ-target]
                        
                    if summ in dict:
                        dict[summ] += 1
                    
                    else:
                        dict[summ] = 1
                        
        return count
                        
                    
                
