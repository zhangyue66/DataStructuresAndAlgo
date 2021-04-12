# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        self.max_depth = 0
        
        def dfs(node,depth):
            if not node:
                return 
            self.max_depth = max(depth,self.max_depth)
            dfs(node.left,depth+1)
            dfs(node.right,depth+1)
            
        #first find max_depth
        dfs(root,0)
        #max_depth = max(value,max_depth)
        #print(self.max_depth)
    
        #second find node in max_depth
        self.ans = 0 
        
        def dfs2(node,depth):
            if not node:
                return
            if depth == self.max_depth:       
                self.ans += node.val
            dfs2(node.left,depth+1)
            dfs2(node.right,depth+1)
            
        dfs2(root,0)
        
        return self.ans
