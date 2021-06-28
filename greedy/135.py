class Solution:
    def candy(self, ratings: List[int]) -> int:
        if len(ratings) == 1:
            return 1
        n = len(ratings)
        left,right = [1]*n,[1]*n
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                left[i] = left[i-1]+1
            
        for j in range(n-2,-1,-1):
            if ratings[j] > ratings[j+1]:
                right[j] = right[j+1]+1
        
        ans = 0
        for k in range(n):
            ans += max(left[k],right[k])
        #print(left,right)
        return ans
                
