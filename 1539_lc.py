class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        cnt = 0
        
        for i in range(1,arr[-1]+1):
            if i not in arr:
                cnt += 1
                
            if cnt == k:
                return i
            
            
        return arr[-1]+(k-cnt)
