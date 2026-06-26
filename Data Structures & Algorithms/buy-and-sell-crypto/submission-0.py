class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        curr_buy = prices[0]
        curr_sell = prices[0]

        for price in prices:
            if price > curr_sell:
                curr_sell = price
                res = max(res, curr_sell - curr_buy)
            if price < curr_buy:
                curr_buy = price
                curr_sell = price
        
        return res