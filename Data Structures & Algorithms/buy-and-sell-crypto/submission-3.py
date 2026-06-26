class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr_buy = float('inf')

        for price in prices:
            if price < curr_buy:
                curr_buy = price
            elif res < price - curr_buy:
                res = price - curr_buy
        
        return res