class Solution:
    def findAnagrams(self, s: str, p: str):
        if p is None or s is None or len(p)> len(s):
            return []


        dic1 = [0]*26
        dic2 = [0]*26
        res = []
        for i in range(len(p)):
            dic1[ord(p[i])-ord('a')] += 1
            dic2[ord(s[i])-ord('a')] += 1
        if dic1 == dic2:
            res.append(0)
        for i in range(1, len(s)-len(p)+1):
            dic2[ord(s[i-1])-ord('a')] -= 1
            dic2[ord(s[i+len(p)-1])-ord('a')] += 1
            if dic1 == dic2:
                res.append(i)
        return res
