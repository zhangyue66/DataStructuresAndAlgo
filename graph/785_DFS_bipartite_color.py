class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # use dfs
        n,colored = len(graph),{}
        
        def dfs(graph,start,colored,c): # c is color
            if start in colored:
                return colored[start] == c
            
            #color the node now as c
            
            colored[start] = c
            
            for node in graph[start]:
                if not dfs(graph,node,colored,1-c):
                    return False
                
            return True
        
        # to handle not connected graph, we need to iterate all node 
        
        for vertex in range(n):
            if vertex not in colored:
                ans = dfs(graph,vertex,colored,1)
                if ans is False:
                    return False
                
        return True
