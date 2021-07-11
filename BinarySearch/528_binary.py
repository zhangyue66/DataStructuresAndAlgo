from random import choices
class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        self.i = [i for i in range(len(w))]

    def pickIndex(self) -> int:
        return choices(self.i,weights=self.w)[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
