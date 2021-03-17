class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        sold,hold = 0,-float("inf") 
        for price in prices:
            hold = max(hold,sold-price)
            sold = max(sold,hold+price-fee)
            
        return sold
