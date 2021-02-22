class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        if X>= Y:
            return X-Y
        
        self.ans = float("inf")
        def backtrack(start,end,op_cnt):
            if start >= end:
                self.ans = min(self.ans,op_cnt+start-end)
                return
            if start ==0:
                return
            
            
            if end % 2 == 1:
                
                backtrack(start,end+1,op_cnt+1)
            else:
                backtrack(start,end //2,op_cnt+1)
                    
                    
        backtrack(X,Y,0)
        return self.ans
