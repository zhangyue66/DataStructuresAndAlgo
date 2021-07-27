# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        ans = []
        
        def backtrack(start,targetSum,cur):
            if not start:
                return
            if not start.left and not start.right:
                if targetSum == start.val:
                    cur.append(start.val)
                    ans.append(cur[:])
                    return
            backtrack(start.left,targetSum-start.val,cur+[start.val])
            backtrack(start.right,targetSum-start.val,cur+[start.val])
            
            
        backtrack(root,targetSum,[])
        
        return ans
