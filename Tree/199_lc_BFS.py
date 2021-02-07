# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return None
        
        ans = []
        
        queue= [(root,0)]
        seen = set()
        
        while queue:
            cur,lvl = queue.pop(0)
            if lvl not in seen:
                ans.append(cur.val)
                seen.add(lvl)
                
            if cur.right:
                queue.append((cur.right,lvl+1))
                
            if cur.left:
                queue.append((cur.left,lvl+1))
                

                
        return ans
