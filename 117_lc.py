"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        def findNext(node):
            if node is None:
                return None
            if node.left:
                return node.left
            if node.right:
                return node.right
            return findNext(node.next)
        
        def dfs(node):
            if node is None:
                return
            if node.left:
                if node.right:
                    node.left.next = node.right
                else:
                    node.left.next = findNext(node.next)
            if node.right:
                node.right.next = findNext(node.next)

            dfs(node.right)
            dfs(node.left)
                
        dfs(root)

        return root
        
