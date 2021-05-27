# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return 
        #first get the linked list length
        length = head
        l = 0
        while length:
            length = length.next
            l += 1
        k %= l
        if k == 0:
            return head
        prev = head
        for i in range(l-k-1):
            prev = prev.next
        #print(prev.val)   
        new_head = prev.next
        prev.next = None
        temp = new_head
        while temp.next:
            temp = temp.next
        temp.next = head
        
        return new_head
            
