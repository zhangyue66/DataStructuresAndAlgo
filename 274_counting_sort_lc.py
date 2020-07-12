class Solution:
    def hIndex(self, citations):
        n = len(citations)
        bucket = [0]*(n+1)
        for _ in citations:
            bucket[min(_,n)] += 1

        ans = n
        s = bucket[n]
        while ans > s:
            ans -= 1
            s += bucket[ans]

        return ans
