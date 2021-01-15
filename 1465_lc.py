class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts):
        horizontalCuts.insert(0,0)
        horizontalCuts.append(h)
        verticalCuts.insert(0,0)
        verticalCuts.append(w)

        horizontalCuts.sort()
        verticalCuts.sort()

        h = 0
        for i in range(len(horizontalCuts)-1):
            h = max(h,horizontalCuts[i+1]-horizontalCuts[i])

        w = 0
        for j in range(len(verticalCuts)-1):
            w = max(w,verticalCuts[j+1]-verticalCuts[j])

        return w*h% 1000000007
yz = Solution()
h = 5
w = 4
horizontalCuts = [1,2,4]
verticalCuts = [1,3]
print(yz.maxArea(h,w,horizontalCuts,verticalCuts))
