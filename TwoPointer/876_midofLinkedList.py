class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        fast,slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow
