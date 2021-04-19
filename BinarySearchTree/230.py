# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # use inorder traversal
        self.nums = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.nums.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return self.nums[k-1]
