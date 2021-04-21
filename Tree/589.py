"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        self.ans = []
        
        def preorder(root):
            if not root:
                return
            self.ans.append(root.val)
            
            for node in root.children:
                preorder(node)
                
        preorder(root)
        
        return self.ans
