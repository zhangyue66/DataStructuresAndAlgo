
from collections import defaultdict

class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        if True not in hasApple:
            return 0

        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])



        searched = set()

        def dfs(graph,node):
            searched.add(node)
            total = 0
            for child in graph[node]:
                if child not in searched:
                    cost = dfs(graph,child)
                    if cost > 0 or hasApple[child]:
                        total += 2 + cost

            return total


        return dfs(graph,0)


n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]
yz = Solution()
print(yz.minTime(n,edges,hasApple))
