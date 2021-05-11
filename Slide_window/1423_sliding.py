class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # sliding window ( window size n-k)
        n = len(cardPoints)
        total = sum(cardPoints)
        
        
        window_sum = sum(cardPoints[:(n-k)])
        ans = total - window_sum
        #print(window_sum,total)
        for i in range(k):
            window_sum = window_sum-cardPoints[i]+cardPoints[i+n-k]
            ans = max(ans,total-window_sum)
            
        return ans
            
