# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.total_sum = 0
        def dfs(root:TreeNode):
            if not root:
                return
            self.total_sum += root.val
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        def calculate_subtree_sum(root):
            if not root:
                return 0
            l = calculate_subtree_sum(root.left)
            r = calculate_subtree_sum(root.right)
            
            subsum = l + r + root.val
            self.ans = max(subsum*(self.total_sum - subsum),self.ans)
            
            return subsum
        
        calculate_subtree_sum(root)
        
        return self.ans%(10**9+7)
