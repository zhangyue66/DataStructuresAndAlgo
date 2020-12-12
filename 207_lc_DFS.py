from collections  import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        self.visited = [0]*numCourses
        self.stack = []

        self.graph = defaultdict(list)

        for pre in prerequisites:
            self.graph[pre[1]].append(pre[0])
        # create adj graph according to prerequitistes


        def dfs(v,visited,stack):
            if visited[v] == 1:
                return 1
            if visited[v] == 2:
                return 0

            visited[v] = 1

            for node in self.graph[v]:

                if dfs(node,visited,stack) == 1:
                    return 1
            self.visited[v] = 2
            stack.append(v)
            return 0

        for v in range(numCourses):
            if self.visited[v] == 0:
                if dfs(v,self.visited,self.stack) == 1:
                    return False
        print(self.stack[::-1])
        return True
