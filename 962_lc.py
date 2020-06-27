class Solution:
    def maxWidthRamp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = sorted(enumerate(A),key = lambda x:x[1])
        #print(A)
        #[(1, 0), (4, 1), (3, 2), (5, 5), (0, 6), (2, 8)] i,_
        # print(A)
        res = 0
        small_loc = A[0][0]
        for i,_ in A:
            if i < small_loc:
                small_loc = i
            else:
                res = max(res,i-small_loc)
        return res

yz = Solution()
A = [6,0,8,2,1,5]
print(yz.maxWidthRamp(A))
