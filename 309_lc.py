class Solution:
    def maxProfit(self, prices):
        if len(prices) == 0:
            return
        sold,rest = 0,0
        hold = -float("inf")

        for price in prices:
            prev_hold = hold
            prev_sold = sold
            hold = max(hold,rest-price)
            sold = prev_hold+price
            rest = max(rest,prev_sold)

        return max(sold,hold,rest)
