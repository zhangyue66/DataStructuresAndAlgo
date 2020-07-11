class Solution:
    def hIndex(self, citations):
        if len(citations) == 0:

            return 0
        # elif len(citations) == 1:
        #     return 1

        ans = []
        citations.sort()

        n = len(citations)

        for i in range(n):
            count = n-i
            if citations[i] >= n-i:
                ans.append(n-i)

        if len(ans) == 0:
            return 0
        else:
            return max(ans)



yz = Solution()
citations = [5]
print(yz.hIndex(citations))
