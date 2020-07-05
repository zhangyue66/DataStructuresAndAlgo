class Solution:
    def findAnagrams(self, s: str, p: str):
        if p is None or s is None or len(p)> len(s):
            return []

        hash_p = {}
        for _ in p:
            if _ not in hash_p:
                hash_p[_] = 1
            else:
                hash_p[_] += 1

        window_size = len(p)
        res = []
        for i in range(len(s)-window_size+1):
            ana = s[i:i+window_size]
            hash_ana = {}
            for _ in ana:
                if _ not in hash_ana:
                    hash_ana[_] = 1
                else:
                    hash_ana[_] += 1
            if hash_ana == hash_p:
                res.append(i)

        return res
