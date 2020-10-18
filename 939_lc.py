class Solution:
    def minAreaRect(self, points):
        hash_x = {}
        xplanes = []

        ans = float("inf")
        for [x,y] in points:
            if x not in hash_x:
                hash_x[x] =[y]
                xplanes.append(x)
            else:
                hash_x[x].append(y)
        for k,v in hash_x.items():
            v.sort()

        xplanes.sort()

        for i in range(len(xplanes)-1):
            for j in range(i+1,len(xplanes)):
                yz = xplanes[j]-xplanes[i]
                print(yz)
                i_h = hash_x[xplanes[i]]
                j_h = hash_x[xplanes[j]]
                for k in range(len(j_h)-1):
                    for l in range(k+1,len(j_h)):
                        if j_h[k] in i_h and j_h[l] in i_h:
                            ans = min(ans,yz*(j_h[l]-j_h[k]))

        if ans == float("inf"):
            return 0
        return ans
yz = Solution()
# points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
print(yz.minAreaRect(points))

