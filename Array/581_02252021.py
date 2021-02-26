class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        sort_num = sorted(nums)
        
        indexs = [0] * len(nums)
        if sort_num == nums:
            return 0
        for i in range(len(nums)):
            if sort_num[i] != nums[i]:
                indexs[i] = 1
                
        # then look for the left most i, and right most j
        left = 0
        for i in range(len(indexs)):
            if indexs[i] == 1:
                left = i
                break
                
        right = 0        
        for j in range(len(indexs)-1,-1,-1):
            if indexs[j] == 1:
                right = j
                break
        print(indexs,left,right)    
        return right-left+1
