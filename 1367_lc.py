# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head, root) -> bool:


        def dfs(root,head):

            if head is None:
                #print("head")
                return True

            if root is None :
                #print("123")
                return False



            if root.val != head.val:
                return False

            a = dfs(root.left,head.next)
            b = dfs(root.right,head.next)
            return a or b

            #print('yz')
            #return False

            #return root.val == head.val and (dfs(root.left,head.next) or dfs(root.right,head.next))



        if head is None:
            return True
        if root is None:
            return False
        return dfs(root,head) or self.isSubPath(head,root.left) or self.isSubPath(head,root.right)


