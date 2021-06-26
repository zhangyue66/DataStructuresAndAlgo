class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [-1]*(n)
        
        def find(a):
            if parent[a] == -1:
                return a
            return find(parent[a])
        
        def union(a,b):
            pa = find(a)
            pb = find(b)
            
            if pa != pb:
                parent[pb] = pa
                
        for edge in edges:
            u,v = edge[0]-1,edge[1]-1
            pu,pv=find(u),find(v)
            if pu == pv:
                return edge
            union(u,v)
