# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        ans = []
        isZigZag = False
        queue = [root]        
        while queue:
            nodes = []
            level = []
            # if isZigZag:
            #     queue = queue[::-1]               
            for node in queue:
                level.append(node.val)
                
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)
            if not isZigZag:
                ans.append(level)
            else:
                ans.append(level[::-1])
            queue = nodes
            isZigZag = not isZigZag          
        return ans
        
