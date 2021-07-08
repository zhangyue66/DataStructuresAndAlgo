# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        l = 1
        l_pointer = root.left
        while l_pointer:
            l_pointer = l_pointer.left
            l += 1
            
        r = 1
        r_pointer = root.right
        while r_pointer:
            r_pointer = r_pointer.right
            r += 1
            
        if l == r:
            return 2**(l) - 1
        return 1+self.countNodes(root.left)+self.countNodes(root.right)
        
