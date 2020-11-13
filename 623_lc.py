# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            ans = TreeNode()
            ans.val = v
            ans.left = root
            return ans
        else:

            queue = [(root,1)]

            while queue:


                (cur,depth) = queue.pop(0)

                
                if depth == d-1:
                    newNode = TreeNode()
                    newNode.val = v
                    newNode.left = cur.left
                    cur.left = newNode
                else:
                    if cur.left:
                        queue.append((cur.left,depth+1))

            
                if depth == d-1:
                    newNode = TreeNode()
                    newNode.val = v
                    newNode.right = cur.right
                    cur.right = newNode
                else:
                    if cur.right:
                        queue.append((cur.right,depth+1))


            return root
