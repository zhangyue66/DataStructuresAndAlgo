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
        
        self.ans = 0
        
        queue = [root]
        
        while queue:
            self.ans = 0

            for i in range(len(queue)):
                node = queue.pop(0)
                self.ans += node.val
                if node.left:
                    queue.append(node.left)    
                if node.right:
                    queue.append(node.right)
                      
        return self.ans
        
