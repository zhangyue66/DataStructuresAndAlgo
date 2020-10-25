class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        
        
        self.res = 0 
        
        def dfs(node,prev):
            if node is None:
                return 
            
            if node.left is None and node.right is None: # reaching leaf node
                self.res += 10* prev + node.val
            prev = 10*prev+node.val
            dfs(node.left,prev)
            dfs(node.right,prev)
        
        dfs(root,0)
        
        return self.res
