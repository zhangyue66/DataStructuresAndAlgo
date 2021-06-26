from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #build a graph from edges, before adding edge , check is u,v already connected,if yes there is cycle
        graph = defaultdict(list)
        
        def is_connected(source,target,visited):
            if source == target:
                return True
            visited.add(source)
            for node in graph[source]:
                if node not in visited:
                    if is_connected(node,target,visited):
                        return True
                    
        for edge in edges:
            u,v = edge[0],edge[1]
            
            visited = set()
            if is_connected(u,v,visited):
                return edge
            
            graph[u].append(v)
            graph[v].append(u)
            
        
        
            
        
