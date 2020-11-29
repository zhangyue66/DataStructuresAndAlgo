class Solution:
    def magicalString(self, n: int) -> int:
        s = "122"  # initial string

        if n <= 3:
            return 1
        fast,slow = 2,2
        while len(s) < n:
            a = int(s[slow])
            b = str(3-int(s[-1]))
            # print(a,b)
            # print(type(a),type(b))
            #s += int(s[fast])*str(3-int(s[slow]))
            s += a*b
            slow += 1
            #fast = len(s) -1

        ans = 0
        #print(s)
        for i in range(n):
            if s[i] == "1":
                ans += 1

        return ans





yz = Solution()
n = 6
print(yz.magicalString(n))
