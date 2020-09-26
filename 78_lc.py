class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        nums.sort()
        
        def backtrack(nums,start,end,res,length):
            if len(res) == length and res not in self.ans:
                self.ans.append(res[:])
                return
            
            
            for i in range(start,end):
                if i !=start and nums[i] == nums[i-1]:
                    continue
                res.append(nums[i])
                backtrack(nums,i+1,end,res,length)
                res.pop()
                
        for k in range(len(nums)+1):    
            backtrack(nums,0,len(nums),[],k)
                
                
        return self.ans
