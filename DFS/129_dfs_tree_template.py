# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(root,num):
            if not root.left and not root.right:
                num += str(root.val)
                self.ans += int(num)
                return
            if root.left:
                dfs(root.left,num+str(root.val))
            if root.right:
                dfs(root.right,num+str(root.val))
            
        dfs(root,"")
        return self.ans
