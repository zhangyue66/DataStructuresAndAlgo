class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.visited =set()
        def backtrack(comb,start,end):
            if len(comb) == len(nums):
                ans.append(comb[:])
                return
            
            for i in range(end):
                if i > start and nums[i] == nums[i-1] and i-1 in self.visited:
                    continue
                if i not in self.visited:
                    comb.append(nums[i])
                    self.visited.add(i)
                    
                    backtrack(comb,start,end)
                    
                    comb.pop()
                    self.visited.remove(i)
                    
        backtrack([],0,len(nums))
        
        return ans
