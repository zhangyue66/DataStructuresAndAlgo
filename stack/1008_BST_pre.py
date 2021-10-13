# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(val=preorder[0])
        if len(preorder) == 1:
            return root
        
        stack = [root]
        
        n = len(preorder)
        for i in range(1,n):
            newNode = TreeNode(val=preorder[i])
            if preorder[i] < stack[-1].val:
                # it is a left node
                stack[-1].left = newNode
                stack.append(newNode)
            else:
                # it is a right node
                parent = stack[-1]
                while stack and preorder[i] > stack[-1].val:
                    parent = stack.pop()
                parent.right = newNode
                stack.append(newNode)
                
        return root
