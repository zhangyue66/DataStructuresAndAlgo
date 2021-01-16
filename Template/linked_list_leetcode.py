class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next


def stringtoLinkedList(input):
    numbers = input
    dummyRoot = ListNode()
    head = ptr = dummyRoot
    for num in numbers:
        ptr.next = ListNode(num)
        ptr = ptr.next

    head = dummyRoot.next

    return head


l1 = [1,2,4]
l2=  [1,3,4]

l1 = stringtoLinkedList(l1)
l2 = stringtoLinkedList(l2)

class Solution:
    def mergeTwoLists(self, l1, l2) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        ans = head = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val :
                head.next = l1
                head = head.next
                l1 = l1.next

            else:
                head.next = l2
                head = head.next
                l2 = l2.next

        if l1:
            head.next = l1
        if l2:
            head.next = l2

        return ans.next

yz = Solution()

res = yz.mergeTwoLists(l1,l2)
nums = []
while res:
    nums.append(res.val)
    res = res.next

print(nums)
