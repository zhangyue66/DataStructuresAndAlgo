class Solution:
    def advantageCount(self, A, B):
        if not A  or not B:
            return []

        ans = []

        A.sort()

        for num in B:
            
            found = False
            for i in range(len(A)):
                if A[i] > num :
                    ans.append(A[i])
                    A.pop(i)
                    found = True
                    break
            
            if found == False:
                ans.append(A.pop(0))


        return ans
