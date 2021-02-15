class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # using set and hash will not hanlde non-connected graph cases 71/78 passed
        # be careful if the node is []/None and not connected to graph
        # a not connected graph is also bipartited so we need to go through all the node
        # if it is a not connected graph , for example there are two cluster. there might be a case
        # when cluster 1 is bipartited but cluster 2 is not .
        n,colored = len(graph),{}
        
        for i in range(n):
            if i not in colored and graph[i]:
                
                queue = [i]
                colored[i] = 1
                while queue:
                    cur = queue.pop(0)
                    for node in graph[cur]:
                        #all neighbor node should be painted with -1
                        if node not in colored:
                            colored[node] = -colored[cur]
                            queue.append(node)
                            
                        elif node in colored:
                            if colored[node] == colored[cur]:
                                return False
        return True
                    
