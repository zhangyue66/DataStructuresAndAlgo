class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        
        i,j = 0,0  #pushed / popped index
        
        for number in pushed:
            
            stack.append(number)
            
            while stack and stack[-1] == popped[j]:
                stack.pop()
                j += 1
                
        if len(stack) == 0 :
            return True
        
        return False
     
class SolutionTwo:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        
        popped.reverse()
        #j = 0 # index of popped
        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[-1]:
                stack.pop()
                popped.pop()
            
        return len(stack) == 0
        
