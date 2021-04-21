"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        # use Queue to do level order traversal
        
        ans = []
        level = set()
        
        if not root:
            return []
        queue = [(root,0)]
        
        while queue:
            
            cur,l = queue.pop(0)
            if l not in level:
                ans.append([cur.val])
                level.add(l)
            else:
                ans[l].append(cur.val)
                
            if cur.children:
                for node in cur.children:
                    queue.append((node,l+1))
                    
        return ans
        
        
