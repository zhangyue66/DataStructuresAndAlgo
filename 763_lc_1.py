class Solution:
    def partitionLabels(self, S):
        hash = {}
        for s in S:
            if s not in hash:
                hash[s] = 1
            else:
                hash[s] += 1

        yz = 0
        cnt = 0
        par = []
        res = []

        for s in S:
            if s not in par:
                par.append(s)
                cnt += hash[s]
                yz += hash[s]
                cnt -= 1
            else:
                cnt -= 1
            if cnt == 0:
                res.append(yz)
                yz = 0
                par = []
        return res
