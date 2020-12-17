#Definition for singly-linked list.
from random import randint
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.number = []
        self.cnt = 0
        while head:
            self.cnt += 1
            self.number.append(head.val)
            head = head.next


    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        choice = randint(0,self.cnt-1)

        return self.number[choice]




# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
