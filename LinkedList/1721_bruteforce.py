# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        nodes = []
        head1 = head
        while head1:
            nodes.append(head1.val)
            head1 = head1.next
            
        nodes[k-1],nodes[-k] = nodes[-k],nodes[k-1]

        head = dummy = ListNode()
        for node in nodes:
            newNode = ListNode(node)
            dummy.next = newNode
            dummy = dummy.next
            
        return head.next
