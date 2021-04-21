# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # use iterative method -> stack
        # preorder root,left,right
        if not root:
            return []
        
        ans = []
        stack = [root]
        
        while stack:
            cur = stack.pop()
            
            ans.append(cur.val)
            
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
                
        return ans
            
            
