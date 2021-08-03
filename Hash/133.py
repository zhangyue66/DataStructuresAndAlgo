"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        newNode = Node(val=node.val,neighbors =[])
        clone_map = {node:newNode}
        def dfs(node):
            for neigh in node.neighbors:
                if neigh not in clone_map:
                    # means this is a new Node.
                    neighCopy = Node(val=neigh.val,neighbors =[])
                    clone_map[neigh] = neighCopy
                    clone_map[node].neighbors.append(neighCopy)
                    dfs(neigh)
                else:
                    clone_map[node].neighbors.append(clone_map[neigh])
            
            return node
        
        dfs(node)
        return newNode
            
