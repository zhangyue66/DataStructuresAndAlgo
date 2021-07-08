class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # find the left most element that has k number of element less than or equal [l,r)
        
        def counting(num):
            # find in matrix that how many no. of element are less than num
            ans = 0
            m,n = len(matrix),len(matrix[0])
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] <= num:
                        ans += 1
            return ans
        
        l,r = matrix[0][0],matrix[-1][-1]+1
        
        while l < r:
            mid = l + (r-l)//2
            
            cnt = counting(mid)
            
            if cnt >= k:
                r = mid
            else:
                l = mid + 1
                
        return l
