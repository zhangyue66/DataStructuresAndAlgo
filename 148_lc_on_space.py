# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        else:
            node_list = []
            
            cur = head
            
            while cur:
                node_list.append(cur.val)
                cur = cur.next
                
            yz = head
            
            node_list.sort()
            
            for i in range(len(node_list)):
                
                yz.val = node_list[i]
                
                yz = yz.next
                
                
            return head
