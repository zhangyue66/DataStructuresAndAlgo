class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # brute force
        ans = []
        
        
        def dfs(graph,node,visited):
            if visited[node] is False:
                visited[node] = True
            for child in graph[node]:
                if visited[child] is False:
                    dfs(graph,child,visited)
                    
        for connection in connections:
            visited = [False]*n
            graph = defaultdict(list)
            for con in  connections:
                if con == connection:
                    continue
                graph[con[0]].append(con[1])
                graph[con[1]].append(con[0])
            
            dfs(graph,0,visited)
            if False in visited:
                ans.append(connection)
                    
        return ans
