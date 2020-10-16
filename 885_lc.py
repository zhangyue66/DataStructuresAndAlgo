class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int):
        matrix =[[0 for i in range(C)] for j in range(R)]

        ans =[[r0,c0]]

        dr = [0,1,0,-1] #east,south,west,north
        dc = [1,0,-1,0] #east,south,west,north
        direction = 0

        step = 0 # when facing east or west : step += 1

        while len(ans) != R*C :
            if direction == 0 or direction == 2:
                step += 1
            for i in range(step):
                r0 += dr[direction]
                c0 += dc[direction]

                if 0<= r0 < R and 0<= c0 < C :
                    ans.append([r0,c0])

                    if len(ans) == R*C:
                        break

            direction = (direction+ 1) % 4

        return ans


yz = Solution()

R = 1
C = 4
r0 = 0
c0 = 0

print(yz.spiralMatrixIII(R,C,r0,c0))
