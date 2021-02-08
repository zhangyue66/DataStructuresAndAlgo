# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        dict = {}
        
        def dfs(node,level):
            if not node:
                return
            
            dfs(node.right,level+1)
            
            if level not in dict:
                dict[level] = node.val
                
            dfs(node.left,level+1)
        
        dfs(root,0)
        ans = []
        for i in range(len(dict)):
            ans.append(dict[i])
            
        return ans
