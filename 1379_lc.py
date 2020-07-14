# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        if not original or not cloned:
            return
        
        else:
            
            queue =[cloned]
            
            while queue:
                
                cur = queue.pop(0)
                
                if cur.val == target.val:
                    return cur
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
                    
            return None
            
