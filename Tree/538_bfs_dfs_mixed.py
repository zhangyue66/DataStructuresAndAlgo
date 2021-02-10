# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.nodes = []
        
        def dfs(node):
            if not node:
                #self.nodes.append(None)
                return
            dfs(node.left)
            if node:
                self.nodes.append(node.val)
            dfs(node.right)
            
        
        dfs(root)
        
        dict = {}
        total = 0
        for i in range(len(self.nodes)-1,-1,-1):
            total += self.nodes[i]
            dict[self.nodes[i]] = total
            
        if not root:
            return
        queue = [root]
        
        while queue:
            cur = queue.pop(0)
            cur.val = dict[cur.val]
            
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
                
        return root
