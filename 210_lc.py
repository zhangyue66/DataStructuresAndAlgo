from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        self.visited =[0]*numCourses
        self.stack = []

        self.graph = defaultdict(list)
        for pre in prerequisites:
            self.graph[pre[1]].append(pre[0])

        def dfs(v,visited,stack):
            if visited[v] == 1 :
                return 1 # means cycle existing

            if visited[v] == 2 :
                return 2

            visited[v] = 1

            for vertex in self.graph[v]:
                if dfs(vertex,visited,stack) == 1:
                    return 1

            visited[v] =2
            stack.append(v)

        for v in range(numCourses):
            if dfs(v,self.visited,self.stack) == 1:
                return []

        if len(self.stack) != numCourses:
            return []
        return self.stack[::-1]



yz =Solution()
numCourses = 2
prerequisites = [[1,0]]
print(yz.findOrder(numCourses,prerequisites))
