# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# idea : https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return root
        else:
            if root.val > key:
                root.left = self.deleteNode(root.left,key)
            elif root.val < key:
                root.right= self.deleteNode(root.right,key)
            else: # root.val = key
                #if target node is leaf
                if root.left is None and root.right is None:
                    return None
                elif root.left is None:#has right child
                    return root.right
                elif root.right is None:#has left child
                    return root.left
                else:#has left and right child - find min in right child and return
                    
                    cur = root.right
                    
                    while cur.left is not None:
                        cur = cur.left
                        
                    root.val = cur.val
                    
                    root.right = self.deleteNode(root.right,cur.val)
                    
            return root
            
        
