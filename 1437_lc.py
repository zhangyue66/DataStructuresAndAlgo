class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if len(nums) == 1:
            return True
        
        index = []
        
        for i in range(len(nums)):
            if nums[i] ==1:
                index.append(i)
                
        if len(index) <= 1:
            return True
        
        for j in range(len(index)-1):
            #check distance between j and j+1
            if index[j+1]-index[j]-1 < k:
                return False
            
        return True
