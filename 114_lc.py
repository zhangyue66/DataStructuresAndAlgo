# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            exit
        else:

            self.val_list = []

            def preorder(node):
                if node is None:
                    return
                else:
                    self.val_list.append(node.val)

                    preorder(node.left)

                    preorder(node.right)

            preorder(root)


            if len(self.val_list) > 1:
                cur = root
                for _ in self.val_list[1:]:
                    new = TreeNode(val=_,left=None,right = None)
                    cur.right = new
                    cur = new

            root.left = None
            
