class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        curA,curB = headA,headB
        while curA != curB:
            if curA:
                curA = curA.next
            else:
                curA = headB
                
            if curB:
                curB = curB.next
                
            else:
                
                curB = headA
                
                
        return curA
