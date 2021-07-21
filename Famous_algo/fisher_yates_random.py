"""
The Fisher-Yates algorithm is remarkably similar to the brute force solution. On each iteration
of the algorithm, we generate a random integer between the current index and the last index of the 
array. Then, we swap the elements at the current index and the chosen index - this simulates drawing (and 
removing) the element from the hat, as the next range from which we select a random index will not include the 
most recently processed one. One small, yet important detail is that it is possible to swap an element with 
itself - otherwise, some array permutations would be more likely than others. 
"""

import random
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.backup = nums[:]

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.nums = self.backup[:]
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        #fisher_yates algo
        n = len(self.nums)
        for i in range(n):
            swap_index = random.randrange(i,n)
            self.nums[i],self.nums[swap_index] = self.nums[swap_index],self.nums[i]
        return self.nums
