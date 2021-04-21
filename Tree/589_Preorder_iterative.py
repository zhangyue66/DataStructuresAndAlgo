"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # use stack to do iterative preorder traversal 
        
        self.ans = []
        
        def iterate(root):
            if not root:
                return
            stack = [root]
            
            while stack:
                cur = stack.pop()
                self.ans.append(cur.val)
                
                for child in cur.children[::-1]:
                    stack.append(child)
                    
        iterate(root)
        
        return self.ans
            
