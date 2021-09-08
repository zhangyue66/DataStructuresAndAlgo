# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init(self):
        self.ans = None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        if head.next is None:
            self.ans = head
            return self.ans
        self.reverseList(head.next)
        temp = head.next
        temp.next = head
        head.next = None
        
        return self.ans
