from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return [0]
        degree = [0]*n
        graph = defaultdict(list)

        for edge in edges:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])


        queue = []

        for i in range(n):
            if degree[i] == 1:
                queue.append(i)


        #print(degree)

        res = []
        while queue:
            target = len(queue)
            ans = []

            for i in range(target):

                v = queue.pop(0)
                ans.append(v)

                for node in graph[v]:
                    degree[node] -= 1
                    if degree[node] == 1:
                        queue.append(node)
            res = ans
        return res
