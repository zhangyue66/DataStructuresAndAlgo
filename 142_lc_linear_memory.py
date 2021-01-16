# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # o (n) memory method using set to mark the node
        checked = set()
        
        while head:
            if head in checked:
                return head
            checked.add(head)
            head = head.next
            
        return None
