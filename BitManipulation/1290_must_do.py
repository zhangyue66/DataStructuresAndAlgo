# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        if not head:
            return
        ans = head.val
        while head and head.next:
            ans = (ans<<1)+head.next.val
            head = head.next
        return ans
