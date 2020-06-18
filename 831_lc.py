class Solution:
    def maskPII(self, S):
        res = ""
        if "@" in S:
            S = S.lower()
            patterns = S.split("@")
            first = patterns[0]
            second = patterns[1]

            res += first[0]+"*****"+first[-1]+"@"+second

            return res
        else:
            for s in S:
                if s.isdigit() == True:
                    res += s

            if len(res) <= 10:
                res = "***-***-"+res[-4:]
            else:
                cnt = len(res) - 10

                res = "+"+"*"*cnt+"-***-***-"+res[-4:]


            return res


yz = Solution()
S =  "86-(10)12345678"   #"1(234)567-890"       #"AB@qq.com"         #"LeetCode@LeetCode.com"
print(yz.maskPII(S))
