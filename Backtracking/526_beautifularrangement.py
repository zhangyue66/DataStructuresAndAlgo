class Solution:
    def countArrangement(self, n: int) -> int:
        self.ans = 0
        
        def backtrack(start,end,nums,n):
            if len(nums) == n:
                self.ans += 1
                return
            
            for i in range(1,n+1):
                if i not in nums:
                    if i%(start+1) ==0 or (start+1)%i == 0:
                        nums.append(i)
                        backtrack(start+1,end,nums,n)
                        nums.pop()
                    
            
        nums = []    
        backtrack(0,n,nums,n)
        return self.ans
