from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        nums = sorted(nums,key=lambda x:(dic[x],-x))
        return nums
          
