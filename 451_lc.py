class Solution:
    def frequencySort(self, s):
        if not s:
            return ""
        ans = ""


        dict = {}

        for str in s:
            if str not in dict:
                dict[str] = 1
            else:
                dict[str] += 1

        sort_freq = []
        keys = []

        for k,v in dict.items():
            sort_freq.append(v)
            keys.append(k)


        sort_freq.sort(reverse=True)

        for fq in sort_freq:
            ele = 0
            for k,v in dict.items():
                if v == fq:
                    ans += v*k
                    ele = k
                    break
            dict.pop(ele)

        return ans


yz = Solution()
s = "tree"
print(yz.frequencySort(s))
