class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        #even pointer and odd pointer
        #even pointer means even index but odd number
        #odd pointer means odd index but even number
        n = len(nums)
        ep,op = 0,1
        while ep < n and op < n:
            while ep < n and nums[ep]%2 == 0:
                ep += 2
            while op < n and nums[op]%2 == 1:
                op+= 2
            if ep < n and op < n:
                nums[ep],nums[op] = nums[op],nums[ep]
        return nums      
