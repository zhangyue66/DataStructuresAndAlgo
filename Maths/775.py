class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        # 0 can be placed at 0 or 1st index 
        # other element can be placed at i-1 or i or i+1 index -> absolut difference between A[i] and i <1
        
        for i in range(len(A)):
            if abs(A[i] - i) >1 :
                return False
            
        return True
