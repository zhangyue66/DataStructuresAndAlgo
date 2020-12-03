import collections
class Solution:
    def isPossible(self, nums):
        if len(nums) < 3:
            return False

        left = collections.Counter(nums)   #Counter({3: 2, 1: 1, 2: 1, 4: 1, 5: 1})
        end = collections.Counter()

        for num in nums:
            if left[num] == 0:
                continue
            left[num] -= 1
            if end[num-1] > 0 :
                end[num-1] -= 1
                end[num] += 1
            elif left[num+1] >0 and left[num+2] > 0:
                left[num+1] -= 1
                left[num+2] -= 1
                end[num+2] += 1
            else:
                return False
        return True
