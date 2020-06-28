class Solution:
    def stoneGame(self, piles):
        n = len(piles)
        
        self.memorization = [[-float("inf") for i in range(n)] for j in range(n)]

        def score(s,l,r):
            if l > r:
                return
            if l == r:
                return s[l]
            else:
                if self.memorization[l][r] == -float("inf"):
                    self.memorization[l][r] = max(s[l]-score(s,l+1,r),s[r]-score(s,l,r-1))
                
                return self.memorization[l][r]

        yz = score(piles,0,n-1)
        
        return yz>0
