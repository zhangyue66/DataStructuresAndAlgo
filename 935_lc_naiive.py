class Solution:
    def knightDialer(self, N: int):
        dir = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
        #dp[3][0] and dp[3][2] will be 0 forever since key is not valid
        dp = [[1 for i in range(3)] for j in range(4)]
        dp[3][0] =dp[3][2] = 0

        for k in range(1,N):
            temp = [[0 for i in range(3)] for j in range(4)]
            for i in range(4):
                for j in range(3):
                    if i ==3 and j !=1:
                        continue
                    else:
                        for d in range(8):
                            tx = j + dir[d][0]
                            ty = i + dir[d][1]
                            if tx <0 or ty <0 or tx >=3 or ty >=4:# knigth jump out of board
                                continue
                            else:
                                temp[i][j] = temp[i][j]+dp[ty][tx]

            dp,temp = temp,dp

        ans = 0
        for i in range(4):
            for j in range(3):
                ans += dp[i][j]

        return ans%(10 ** 9 + 7)

yz = Solution()
N = 500
print(yz.knightDialer(N))
