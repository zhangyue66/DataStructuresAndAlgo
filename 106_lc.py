# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 0 or len(postorder) == 0 or len(inorder) != len(postorder):
            return None
        else:
            hash_in = {}
            for i in range(len(inorder)):
                hash_in[inorder[i]] = i
                
            def helper(inorder,postorder,inStart,inEnd,postStart,postEnd,hash_in):
                if inStart > inEnd or postStart > postEnd:
                    return None
                else:
                    
                    root = TreeNode(val = postorder[postEnd],left = None,right = None)
                    
                    rootIndex = hash_in[postorder[postEnd]]
                    
                    root.left = helper(inorder,postorder,inStart,rootIndex-1,postStart,postStart+rootIndex-1-inStart,hash_in)
                    
                    root.right = helper(inorder,postorder,rootIndex+1,inEnd,postStart+rootIndex-1-inStart+1,postEnd-1,hash_in)
                    
                    return root
                
                
            return helper(inorder,postorder,0,len(inorder)-1,0,len(postorder)-1,hash_in)
        
        
                    
        
        
