class Solution:
    def processQueries(self, queries, m):
        perm =[i for i in range(1,m+1)]

        ans = []

        for query in queries:
            yz = perm.index(query)
            ans.append(yz)
            first = perm.pop(yz)
            perm.insert(0,first)



        return ans


yz = Solution()
queries = [7,5,5,8,3]
m = 8
print(yz.processQueries(queries,m))
