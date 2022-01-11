# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(root,num_str):
            if not root:
                return
            if not root.left and not root.right:
                # reaching the leaf
                num_str += str(root.val)
                self.ans += int("0b"+num_str,2)
            dfs(root.left,num_str+str(root.val))
            dfs(root.right,num_str+str(root.val))
            
        dfs(root,"")
        return self.ans
