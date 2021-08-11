class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        # l[i] ~ from 0 to i # of 0s -> count # of 1s
        # r[i] ~ from i to n-1 # of 1s -> count # of 0s
        left,right = [0]*n,[0]*n
        cnt1,cnt0 = 0,0
        
        if s[0] == "0":
            left[0] = 0
        else:
            left[0] = 1
            cnt1 += 1
        for i in range(1,n):
            if s[i] == "1":
                cnt1 += 1
            left[i] = cnt1
        # if s[n-1] == "1":
        #     right[n-1] = 0
        # else:
        #     right[n-1] = 1
        #     cnt0 += 1
        for j in range(n-1,-1,-1):
            if s[j] == "0":
                cnt0 += 1
            right[j] = cnt0
        #print(left,right)
        ans = min(left[n-1],right[0])
        for k in range(1,n):
            flip = left[k-1]+right[k]
            ans = min(flip,ans)
        return ans
