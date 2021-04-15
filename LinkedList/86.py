# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return 
        ans= part_one = ListNode()
        temp = part_two = ListNode()
        
        while head:
            if head.val < x:
                part_one.next=ListNode(head.val)
                part_one = part_one.next
            else:
                part_two.next=ListNode(head.val)
                part_two = part_two.next
                
            head = head.next
            
        part_one.next=temp.next
        
        return ans.next
