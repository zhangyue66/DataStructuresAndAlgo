from _collections import defaultdict

class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites, queries):
        self.graph = defaultdict(list)

        for pre in prerequisites:
            self.graph[pre[1]].append(pre[0])
        print(self.graph)


        self.yz = [[] for i in range(n)]

        def bfs(s):
            visited = [False]*n
            queue = [s]
            visited[s] = True

            while queue:
                cur = queue.pop(0)
                self.yz[s].append(cur)

                for i in self.graph[cur]:
                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True

        for i in range(n):
            bfs(i)
            print(self.yz)

        #return self.yz  # [[0, 1], [1]]
        print(self.yz)

        ans = []
        for query in queries:
            if len(self.yz[query[1]]) == 1:
                ans.append(False)
            else:
                if query[0] in self.yz[query[1]]:
                    ans.append(True)
                else:
                    ans.append(False)

        return ans



yz =Solution()
n = 5
prerequisites = [[0,1],[1,2],[2,3],[3,4]]
queries = [[0,4],[4,0],[1,3],[3,0]]
print(yz.checkIfPrerequisite(n,prerequisites,queries))
