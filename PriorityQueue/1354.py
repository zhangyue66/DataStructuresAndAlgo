class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # recursion approach
        n = len(target)
        sum = 0
        max_index = 0
        
        for i in range(n):
            sum += target[i]
            if target[max_index] < target[i]:
                max_index = i
        
        
        
        diff = sum - target[max_index]
        if target[max_index] == 1 or diff == 1:
            return True
        
        if diff > target[max_index] or diff == 0  or target[max_index]%diff == 0:
            return False
        
        
        target[max_index] %= diff
        
        return self.isPossible(target)
