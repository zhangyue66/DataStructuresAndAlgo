from random import shuffle
class Solution:

    def __init__(self, nums: List[int]):
        self.backup =  []
        for num in nums:
            self.backup.append(num)
         
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.backup

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        self.nums = self.backup[::]
        shuffle(self.nums)
        return self.nums


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
