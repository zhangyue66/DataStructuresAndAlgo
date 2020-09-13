class Solution:
    def freqAlphabets(self, s):
        dic = {"1":"a","2":"b","3":"c","4":"d","5":"e","6":"f","7":"g","8":"h","9":"i","10":"j","11":"k","12":"l","13":"m","14":"n","15":"o","16":"p","17":"q","18":"r","19":"s","20":"t","21":"u","22":"v","23":"w","24":"x","25":"y","26":"z"}

        n = len(s)-1
        ans=""
        while n >= 0:
            if s[n] == "#":
                yz = dic[s[n-2:n]]
                ans += yz
                n -= 3

            else:
                yz = dic[s[n]]
                ans += yz
                n -= 1
        return ans[::-1]
yz = Solution()
s = "10#11#12"
print(yz.freqAlphabets(s))
