# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:
        
        res = []
        
        if root is None:
            return
        
        queue = [root]
        
        while queue:
            cur = queue.pop(0)
            
            if type(cur.val) == int:
                cur.val = chr(ord("a")+cur.val)
            
            if not cur.left and not cur.right:
                res.append(cur.val)
                
            if  cur.left:
                cur.left.val = chr(ord("a")+cur.left.val)+cur.val
                queue.append(cur.left)
                
            if cur.right:
                cur.right.val = chr(ord("a")+cur.right.val)+cur.val
                queue.append(cur.right)
                
        res.sort()
        
        return res[0]
        
