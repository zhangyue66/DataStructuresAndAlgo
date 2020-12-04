from collections import defaultdict

class Solution:
    def loudAndRich(self, richer, quiet):
        n = len(quiet)
        graph = defaultdict(list)
        for i in range(n):
            graph[i].append(i)
        for rich,poor in richer:
            graph[poor].append(rich)

        #print(graph)  ->defaultdict(<class 'list'>, {0: [0, 1], 1: [1, 2, 3], 2: [2], 3: [3, 4, 5, 6], 4: [4], 5: [5], 6: [6], 7: [7, 3]})
        ans = []

        #DFS
        self.res = float("inf")
        self.cur = "#"
        def dfs(graph,node,searched):

            if node not in searched:
                value = quiet[node]
                if value < self.res:
                    self.cur = node
                    self.res = value

                searched.add(node)
            for vert in graph[node]:
                if vert not in searched:
                    dfs(graph,vert,searched)




        for i in range(n):

            dfs(graph,i,set())
            ans.append(self.cur)
            self.res = float("inf")
            self.cur = "#"

        return ans


yz = Solution()
richer = [[1,0],[2,1],[3,1],[3,7],[4,3],[5,3],[6,3]]
quiet = [3,2,5,4,6,1,7,0]
print(yz.loudAndRich(richer,quiet))
